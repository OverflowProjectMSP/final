from app import *
# from app import HOST_PG, USER_PG, PASSWORD_PG, PORT_PG
from render_and_adding import add_img
import os
import uuid
import psycopg2
from psycopg2 import Error
from flask import jsonify, request, session
import smtplib
from email.mime.text import MIMEText
import random
from datetime import datetime
from dotenv import load_dotenv
import logging
from email.message import EmailMessage
import requests as req

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("user.py have connected")

# Обновление доп данных о
def refresh_data(info, id):
    data = ''
    for i in info:
        if info[i] != 'false':
            if i == 'avatar' or i == 'filename':
                continue
            if data == '':
                data += f' {i}=$${info[i]}$$'
            else:
                data += f', {i}=$${info[i]}$$'

    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if 'filename' in info:
            src = add_img(info['avatar'], info['filename'], True, False, session.get('id') )
            data+= f', avatar=$${src}$$'
        print(data)
        cursor.execute(f"""UPDATE users 
                    SET {data}
                    WHERE id=$${id}$$;""")
        pg.commit()

        return_data = "Ok"
        logging.info('Данные о пользотвател обновлены')

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# LogIn
def login_user(email, pas):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"SELECT COUNT(*) FROM users WHERE email=$${email}$$")

        # Проверка есть ли такой пользователь
        if cursor.fetchall()[0][0]==1:

            cursor.execute(f"SELECT * FROM users WHERE email=$${email}$$")
            user = cursor.fetchone()


            # Проверка пароля
            if user[3] == pas:
                return_data = user[2]

                logging.info(f"Вход выполнен! Здравствуйте, {user[2]}")
                return_data=['ok', user[0]]

            else:
                logging.warning("Неверный пароль!")
                return_data = 'Неверный пароль!'
        else:
            logging.warning("Аккаунта с такой почтой не существует!")
            return_data = "Аккаунта с такой почтой не существует!"

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Регистрация пользователя
def add_user_todb(name, email, pas):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        send_user = []
        cursor.execute(f"SELECT COUNT(*) FROM users WHERE username=$${name}$$")
        send_user.append(cursor.fetchone())

        cursor.execute(f"SELECT COUNT(*) FROM users WHERE email=$${email}$$")
        send_user.append(cursor.fetchone())
        # Проверка существует ли такой пользователь
        if send_user[0][0] == 0 and send_user[1][0] == 0:
            rand_avatar = random.randint(1, 12)
            user_to_write = (uuid.uuid4().hex, name, email, pas, '', '', '', '', '', '', '', '', '', '', '', '', '', f'http://api.upfollow.ru/avatar/default_avatar_{rand_avatar}', False, datetime.now().isoformat(), 0, 'Амеба')

            cursor.execute(f"""INSERT INTO users(id, username, email, password, name, surname, interestings, about, country, region, city, telegram, skype, discord, facebook, phonenumber, github, avatar, admin, data_c, c_active, rang) VALUES {user_to_write}""")

            pg.commit()

            logging.info("Пользователь зарегестрирован!")
            return_data = 'Ok'

        else:
            return_data = "Пользователь с таким именем или почтой уже существует!"
            logging.warning(return_data)

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Изменения пароля, если user знает страый
def change_password(password, old_password, id):
    if check_old_password( id ,old_password): # Вернет True если пароли стовпадает со старым
        try:
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f'''UPDATE users
                            SET password=$${password}$$
                            WHERE id=$${id}$$;
                            ''')
            pg.commit()

            logging.info(f'Пароль изменен на {id}')

            return_data = "True"


        except (Exception, Error) as error:
            logging.error('DB:', error)
            return_data = f"Ошибка получения данных: {error}"

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data
    else: return_data = "False"

# Проверка совпадениеия старого пароля с ныненшним
def check_old_password(id, password):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f'SELECT password FROM users WHERE id=$${id}$$')
        password_to_check = cursor.fetchone()
        print(password_to_check, password)
        if password_to_check[0] == str(password):
            return_data = True
            logging.info('Пароли не совпадают')
        else: return_data = False

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Измения пароля с праолем на email
def change_password_send(password, email):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        print(f'''UPDATE users
                SET password=$${password}$$
                WHERE email=$${email}$$;
                ''')

        cursor.execute(f'''UPDATE users
                        SET password=$${password}$$
                        WHERE email=$${email}$$;
                        ''')
        pg.commit()
        return_data = "True"
        logging.info(f'Пароль изменен на {email}')



    except (Exception, Error) as error:
        logging.error(f"Ошибка получения данных: {error}" )
        return_data = "Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Отпрака кода на почту
def send_code(email):
    message_1 = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title></title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet">
    <style>
    * {
        margin: 0;
        font-family: "Rubik", system-ui;
    }

    @media (max-width: 500px) {
        .window {
        width: 370px;
        }

        h1 {
        font-size: 21px;
        }

        p {
        font-size: 10px;
        }

        h2 {
        font-size: 22px;
        width: 30px;
        }
    }
    
    
    </style>
    </head>"""

    sender = "upfollow835@gmail.com"
    send_password = "zwrx qgne arwj jblp"

    code_pas = ""
    
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    code_pas = str(a) + str(b) + str(c) + str(d)

    message_2 = f"""<body style="width: 100%">
        <div style="width: 100%; height: 450px; text-align: center; font-family: 'Rubik', system-ui;">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td align="center">
                        <h1 style="color: #3b82f6; border-bottom: 3px solid #3b82f6; padding-bottom: 20px; margin-bottom: 20px; text-align: center; width: 500px;">UpFollow</h1>
                    </td>
                </tr>
            </table>
            <p style="color: #3b82f6; font-weight: 600; font-size: 13px; margin-bottom: 60px;">Здравствуйте!</p>
            <p style="color: #3b82f6; font-weight: 600; font-size: 13px; margin-bottom: 40px;">Для сброса пароля введите в поле этот код:</p>
            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:20px;">
                <tr>
                    <td align="center">
                        <table width="20%" border="0" cellspacing="0" cellpadding="0"" style="border: 2px solid black; border-radius: 8px; padding:16px 10px; background-color: #E2EEFF">
                            <tr>
                                <td align="center">
                                    <td align="center"><h2>{a}</h2></td> <td align="center"><h2>{b}</h2></td> <td align="center"><h2>{c}</h2></td> <td align="center"><h2>{d}</h2></td>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td align="center">
                        <p style="color: #3b82f6; font-weight: 600; font-size: 13px; text-align: center;">
                            Пожалуйста! Обратите внимание, кто-то пытается сбросить ваш пароль. <br>
                            Если это были не вы, срочно поменяйте пароль от вашего <br>
                            аккаунта на форуме UpFollow!
                        </p>

                        <p style="border-top: 3px solid #3b82f6; padding-top: 20px; color: #3b82f6; font-weight: 600; font-size: 13px; text-align: center; width: 500px; margin-top: 30px;">
                            Спасибо, что остаетесь с нами! <br> С заботой о Вас, команда UpFollow
                        </p>
                    </td>
                </tr>
            </table>
        </div>
    </body>
    </html>"""

    msg = EmailMessage()

    msg["Subject"] = "Ваш код"
    msg["From"] = sender
    msg["To"] = email
    msg.set_content("Код для подтверждения регистрации")
    msg.add_alternative(message_1 + message_2, subtype="html")
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, send_password)
        server.send_message(msg)
        logging.info("Email sent successfully!")
    except smtplib.SMTPRecipientsRefused:
        logging.info("Error: Recipient's email does not exist.")
        return 1
    finally:
        server.quit()
        # держим пароль в сессии
        session['code'] = str(code_pas)
        session.modified = True
        session['email'] = str(email)
        session.modified = True

        logging.info(f'Пароль {code_pas} отправлен на почту {email}')

        return 0

# Проверка совпадения кода с Frontend и реального кода
def check_password(password, true_password):
    print(password, type(password), true_password, type(true_password))
    if password == true_password:
        return_data = 'True'
        logging.info('Пароли совпали')
    else:
        logging.info('Пароли не совпали')
        return_data = 'False'
    session.pop('sent-password', None)
    return return_data

# показ всего о юзере
def show_user_info(id, isAll):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from users WHERE id=$${id}$$")

        all_states = dict(cursor.fetchall()[0])
        logging.info('Инфа есть')
        return_data={}

        for key in all_states:
            if key != "password":
                return_data[key] = all_states[key]

        return_data['data_c'] = datetime.strftime(return_data['data_c'], '%d %B %Y')

        if not isAll:
            # счетчик статей
            cursor.execute(f"SELECT COUNT(*) from states WHERE id_u=$${id}$$")
            return_data['scnt'] = cursor.fetchone()[0]

            # счетчик вопросов
            cursor.execute(f"SELECT COUNT(*) from questions WHERE id_u=$${id}$$")
            return_data['qcnt'] = cursor.fetchone()[0]

            # счетчик ответов и комментариев
            cursor.execute(f"SELECT COUNT(*) from answers WHERE id_u=$${id}$$")
            cnt_a = cursor.fetchone()[0]

            cursor.execute(f"SELECT COUNT(*) from comments WHERE id_u=$${id}$$")
            cnt_c = cursor.fetchone()[0]

            return_data['acnt'] = cnt_a + cnt_c

        logging.info(f'Инофрмация профиля {id} отображена')
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# показ id avtar name
def show_not_all(id):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''SELECT id, username, avatar FROM users
                      WHERE id = $${id}$$''')

        info = dict(cursor.fetchall()[0])
        return_data = {}

        for key in info:
            return_data[key] = info[key]

        logging.info(f'Неполная инофрмация профиля {id} отображена')


    except (Exception, Error) as error:
        logging.error(f"Ошибка получения данных: {error}")
        return_data = 'No'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

def auth_tg(hash_id, uf_id):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM tg_hashs WHERE id_hash=$${hash_id}$$")
        result = cursor.fetchall()
        if len(result) != 0:
            result = dict(result[0])
            if sub_time(result["time"]) and uf_id:
                cursor.execute(f"UPDATE users SET tg_id=$${result['tg_id']}$$, tg_chat_id=$${result['chat_id']}$$ WHERE id=$${uf_id}$$")
                return_data = "all ok"
            elif not sub_time(result["time"]):
                result = {"chat_id": -1}
                return_data = "Время жизни ссылки истекло"
            else:
                result = {"chat_id": -1}
                return_data = "Пользователь не в аккаунте"
        else:
            result = {"chat_id": -1}
            return_data = "Невалидная ссылка"

            # TODO: добавить в бд столбец-статус - ссылка уже использованна
    except (Exception, Error) as error:
        logging.error(f"Ошибка получения данных: {error}")
        return_data = 'Err'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data, result["chat_id"]

def tg_sendMessage(chat_id, text):
    url=f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': "Поздравляю с успешной ауентифкацией на сайте"
    }
    res = req.post(url, data=payload)
    if not res.ok:
        logging.info(res)
        return "err"
    return "ok"

def send_pas_code(email):
    message_1 = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title></title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet">
    <style>
    * {
        margin: 0;
        font-family: "Rubik", system-ui;
    }

    @media (max-width: 500px) {
        .window {
        width: 370px;
        }

        h1 {
        font-size: 21px;
        }

        p {
        font-size: 10px;
        }

        h2 {
        font-size: 22px;
        width: 30px;
        }
    }
    
    
    </style>
    </head>"""

    sender = "upfollow835@gmail.com"
    send_password = "zwrx qgne arwj jblp"

    code_pas = ""
    
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    code_pas = str(a) + str(b) + str(c) + str(d)

    message_2 = f"""<body style="width: 100%">
        <div style="width: 100%; height: 450px; text-align: center; font-family: 'Rubik', system-ui;">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td align="center">
                        <h1 style="color: #3b82f6; border-bottom: 3px solid #3b82f6; padding-bottom: 20px; margin-bottom: 20px; text-align: center; width: 500px;">UpFollow</h1>
                    </td>
                </tr>
            </table>
            <p style="color: #3b82f6; font-weight: 600; font-size: 13px; margin-bottom: 60px;">Добро пожаловать на наш форум!</p>
            <p style="color: #3b82f6; font-weight: 600; font-size: 13px; margin-bottom: 40px;">Для завершения регистрации введите в поле этот код:</p>
            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:20px;">
                <tr>
                    <td align="center">
                        <table width="20%" border="0" cellspacing="0" cellpadding="0"" style="border: 2px solid black; border-radius: 8px; padding:16px 10px; background-color: #E2EEFF">
                            <tr>
                                <td align="center">
                                    <td align="center"><h2>{a}</h2></td> <td align="center"><h2>{b}</h2></td> <td align="center"><h2>{c}</h2></td> <td align="center"><h2>{d}</h2></td>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td align="center">
                        <p style="color: #3b82f6; font-weight: 600; font-size: 13px; text-align: center;">
                            Пожалуйста! Обратите внимание, кто-то пытается зарегистрироваться с помощью данной почты. <br>
                            Если это были не вы, просто проигнорируйте это сообщение.
                        </p>

                        <p style="border-top: 3px solid #3b82f6; padding-top: 20px; color: #3b82f6; font-weight: 600; font-size: 13px; text-align: center; width: 500px; margin-top: 30px;">
                            Спасибо, что остаетесь с нами! <br> С заботой о Вас, команда UpFollow
                        </p>
                    </td>
                </tr>
            </table>
        </div>
    </body>
    </html>"""

    msg = EmailMessage()

    msg["Subject"] = "Ваш код"
    msg["From"] = sender
    msg["To"] = email
    msg.set_content("Код для подтверждения регистрации")
    msg.add_alternative(message_1 + message_2, subtype="html")
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, send_password)
        server.send_message(msg)
        logging.info("Email sent successfully!")
    except smtplib.SMTPRecipientsRefused:
        logging.info("Error: Recipient's email does not exist.")
        return 1, 0, 0
    finally:
        server.quit()
        # держим пароль в сессии


        logging.info(f'Пароль {code_pas} отправлен на почту {email}')

        return 0, str(code_pas), str(email)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Регистрация
@app.route('/registration', methods=['POST'])
def user_registration():
    response_object = {'status': 'success'} #БаZа
    if "code" in session:
        response_object["res"] = "вам уже был направлен код"
        return jsonify(response_object)
    session["code"] = "0"
    post_data = request.get_json()
    res, code, email = send_pas_code(post_data.get('email'))
    session.pop("code", None)
    if res == 0:
        session["code"] = code
        session.permanent = True
        session.modified = True
        session["email"] = email
        session.modified = True
        session["name"] = post_data.get('name')
        session.modified = True
        session['password'] = post_data.get('password')
        session.modified = True
        response_object["res"] = "Ok"
    else: response_object["res"] = "Некорректная почта"
        # logging.info(add_user_todb(post_data.get('name'), post_data.get('email'), post_data.get('password'))) #Вызов фунции добавления пользователя в бд и ее debug

    return jsonify(response_object)

def add_img_f(file, name):
    # name = file.filename
    try:
        logging.info(file)
        file.save(os.path.join(AVATAR, name))
        return_data = 'https://api.upfollow.ru/avatar/'+name
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = error
    finally:
        return return_data

@app.route("/reg-code-send", methods=["POST"])
def reg_fhjfhf():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()
    logging.info(session.get("code"))
    logging.info(post_data.get("emailCode"))
    if session.get("code") == post_data.get("emailCode"):
        res = add_user_todb(session.get('name'), session.get('email'),session.get('password')) #Вызов фунции добавления пользователя в бд и ее debug
        response_object["res"] = res
        logging.info(res)
        session.pop("code", None)
        session.pop("name", None)
        session.pop("email", None)
        session.pop("password", None)
    else: response_object["res"] = "Некорректный код"

    return jsonify(response_object)
# def refresh_data_tset(info, id):
#     data = ''
#     for i in info:
#         if info[i] != 'false':
#             if i == 'avatar' or i == 'filename':
#                 continue
#             if data == '':
#                 data += f' {i}=$${info[i]}$$'
#             else:
#                 data += f', {i}=$${info[i]}$$'

#     try:
#         pg = psycopg2.connect(f"""
#             host={HOST_PG}
#             dbname=postgres
#             user={USER_PG}
#             password={PASSWORD_PG}
#             port={PORT_PG}
#         """)

#         cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         if 'filename' in info:
#             src = add_img_t(info['avatar'], info['filename'], True, False, session.get('id'), True)
#             data+= f', avatar=$${src}$$'
#         print(data)
#         cursor.execute(f"""UPDATE users
#                     SET {data}
#                     WHERE id=$${id}$$;""")
#         pg.commit()

#         return_data = "Ok"
#         logging.info('Данные о пользотвател обновлены')

#     except (Exception, Error) as error:
#         logging.error(f'DB: ', error)
#         return_data = f"Error"

#     finally:
#         if pg:
#             cursor.close
#             pg.close
#             logging.info("Соединение с PostgreSQL закрыто")
#             return return_data

#Изменение информации пользователя
@app.route('/user-info', methods=['GET', 'PUT'])
def user_info():
    response_object = {'status': 'success'} #БаZа

    if request.method == 'PUT':
        post_data = request.get_json()
        #Вызов функции обновления бд
        post_data = post_data.get('form')
        refresh_data(post_data, session.get('id'))

        return jsonify(response_object)

    print(request.args.get('id'))
    response_object['all'] = show_user_info(request.args.get('id'), False)
    print(response_object)
    return jsonify(response_object)



#Изменение информации пользователя
@app.route('/user-info-r', methods=['GET'])
def user_info__():
    response_object = {'status': 'success'} #БаZа

    print(request.args.get('id'))

    response_object['all'] = show_user_info(request.args.get('id'), True)

    print(response_object)

    return jsonify(response_object)
#Вход
@app.route('/login', methods=['GET', 'POST'])
def login():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()
    a = login_user(post_data.get('email'), post_data.get('password'))
    if a[0] == "ok": #Вызов и debug функции проверки пароля пользователя (вход в аккаунт)
        session['id'] = a[1]
        session.permanent = True
        session.modified = True
        response_object['message'] = 'ok'

    else: response_object['message'] = 'wrong!'
    return response_object

#Обновление пароля
@app.route('/new-password-old', methods=['PUT'])
def new_password_with_old():

    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    #Вызов, debug и возврат ответа на клиент функции обновления пароля
    if request.method=='PUT':
        print(session.get('id'))
        response_object['res'] = change_password(post_data.get('new_password'),post_data.get('old_password'), session.get('id'))
        logging.info(response_object['res'])

    return jsonify(response_object)

#Восстановление пароля
@app.route('/new-password-email', methods=['POST', 'PUT'])
def new_password_with_email():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    if request.method=='PUT':
        #Восстановление пароля если мы в аккаунте
        print(post_data.get('password'), session.get('email'))
        response_object['res'] = change_password_send(post_data.get('password'), session.get('email'))
    # if post_data.get("email") is None:
    elif request.method == 'POST' and post_data.get('email'):
        logging.info(post_data.get("email"))
        #Восстановление пароля если мы НЕ в аккаунте
        send_code(post_data.get('email'))

    else:
        # ХЗ, вроде проверка кода подтверждения
        response_object['res'] = check_password(post_data.get('emailCode'), session.get('code'))

    return jsonify(response_object)


# может ли юзер удалять/менять или нет

# показ id avtar name
@app.route('/user-not-all', methods=['GET'])
def user__():
    response_object = {'status': 'success'} #БаZа

    response_object['all'] = show_not_all(request.args.get('id'))

    return jsonify(response_object)

def get_top():
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute("""SELECT 
                        u.id, 
                        u.username, 
                        u.avatar,
                        COALESCE(c.comment_count, 0) AS comment_count, 
                        COALESCE(a.answer_count, 0) AS answer_count,
                        COALESCE(c.comment_count, 0) + COALESCE(a.answer_count, 0) AS total_count
                    FROM 
                        users u
                    LEFT JOIN 
                        (SELECT id_u, COUNT(*) AS comment_count FROM comments GROUP BY id_u) c ON u.id = c.id_u
                    LEFT JOIN 
                        (SELECT id_u, COUNT(*) AS answer_count FROM answers GROUP BY id_u) a ON u.id = a.id_u
                    ORDER BY 
                        total_count DESC
                    LIMIT 10;""")

        r = cursor.fetchall()
        return_data = []
        for row in r:
            a = dict(row)
            return_data.append(a)

    except (Exception, Error) as error:
        logging.error(f"Ошибка получения данных: {error}")
        return_data = 'No'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

@app.route("/get-top", methods=["GET"])
def top():
    response_object = {'status': 'success'} #БаZа

    response_object['all'] = get_top()

    return jsonify(response_object)

@app.route("/get-curent-avatar", methods=["GET"])
def get_curent_avatar():
    response_object = {'status': 'success'} #БаZа

    if 'id' in session:
        response_object['all'] = show_not_all(session.get("id"))
    else:
        response_object['all'] = None

    return jsonify(response_object)
