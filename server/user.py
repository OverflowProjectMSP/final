from app import *
# from app import HOST_PG, USER_PG, PASSWORD_PG, PORT_PG
from render_and_adding import add_img
import os
import uuid
import psycopg2
from psycopg2 import extras, Error
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
import random
from datetime import datetime
from dotenv import load_dotenv
import base64
import logging
import asyncio

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
            user_to_write = (uuid.uuid4().hex, name, email, pas, '', '', '', '', '', '', '', '', '', '', '', '', '', 'https://api.upfollow.ru/avatar/AvatarDef.png', False, datetime.now().isoformat())

            cursor.execute(f"""INSERT INTO users(id, username, email, password, name, surname, interestings, about, country, region, city, telegram, skype, discord, facebook, phonenumber, github, avatar, admin, data_c) VALUES {user_to_write}""")

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
    sender = "upfollow835@gmail.com"
    send_password = "zwrx qgne arwj jblp"

    code_pas = ""

    # ------------------------Улучшить бы----------------------------------------------------
    for _ in range(4):
        a = random.randint(0, 9) # А че тут улучшать? (Без негатива, от febolo)
        code_pas += str(a)
    #-----------------------------------------------------------------------------------------

    msg = MIMEText(f"Ваш код для изменения пароля: {code_pas}. Не сообщайте его никому!")
    msg["Subject"] = "Ваш код"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender, send_password)

    server.sendmail(sender, email, msg.as_string())

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

def sub_time(timestamp):
    timestamp = str(timestamp)
    logging.info(timestamp)
    timestamp = timestamp.replace("<", "").replace(">", "").replace(":", "")  # remove extra chars

    year = timestamp[:4]
    month = timestamp[5:7]
    day = timestamp[8:10]
    hour = timestamp[11:13]
    minute = timestamp[13:15]

    dt = datetime(int(year), int(month), int(day), int(hour), int(minute))
    current_time = datetime.now()

    return dt > current_time


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
                cursor.execute(f"UPDATE users SET tg_id=$${result["tg_id"]}$$, tg_chat_id=$${result["chat_id"]}$$ WHERE id=$${uf_id}$$")
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
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Регистрация
@app.route('/registration', methods=['GET', 'POST'])
def user_registration():
    response_object = {'status': 'success'} #БаZа
    if request.method == 'POST':
        post_data = request.get_json()
        logging.info(add_user_todb(post_data.get('name'), post_data.get('email'), post_data.get('password'))) #Вызов фунции добавления пользователя в бд и ее debug

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

    elif request.method == 'POST' and post_data.get('email'):
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


