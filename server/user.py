from app import *


load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)
 
print("OK")

# Обновление доп данных о 
def refresh_data(info, id):
    data = ''
    for i in info:
        logging.info(i)
        if info[i] != 'false':
            if i == 'avatar' or i == 'filename':
                continue
            if data == '':
                data += f' {i}=$${info[i]}$$'
            else:
                data += f', {i}=$${info[i]}$$'

    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        # src = add_img(info['avatar'], info['filename'], True, False, session.get('id') )
        # UPDATE user-info
        cursor.execute(f"""UPDATE users 
                    SET {data}
                    WHERE id='f527d19af56b4614bab663800ed79825';""")
        pg.commit()

        return_data = "Данные изменены"

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

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
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
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
        return_data = f"Ошибка обращения к базе данных: {error}" 

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
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        send_user = []
        cursor.execute(f"SELECT COUNT(*) FROM users WHERE username=$${name}$$")  
        send_user.append(cursor.fetchone())

        cursor.execute(f"SELECT COUNT(*) FROM users WHERE email=$${email}$$")
        send_user.append(cursor.fetchone())
        # Проверка существует ли такой пользователь
        if send_user[0][0] == 0 and send_user[1][0] == 0:
            user_to_write = (uuid.uuid4().hex, name, email, pas, False)
            
            cursor.execute(f"INSERT INTO users(id, username, email, password, admin) VALUES {user_to_write}")      
            
            pg.commit()
            
            return_data = "Пользователь зарегестрирован!"

        else:
            return_data = "Пользователь с таким именем или почтой уже существует!"
            logging.warning(return_data)

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Ошибка добавления в базу данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
 
# Изменения пароля, если user знает страый
def change_password(password, old_password, id):
    try: 
        if check_old_password(old_password, id): # Вернет True если пароли стовпадает со старым 
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

            logging.info('Пароль изменен')

            return_data = "True"

        else: return_data = "False"

    except (Exception, Error) as error:
        logging.error('DB:', error)
        return_data = f"Ошибка получения данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Проверка совпадениеия старого пароля с ныненшним
def check_old_password(id, password):
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        password_to_check = cursor.execute(f'SELECT password FROM users WHERE id=$${id}$$')

        if password_to_check == password:
            return_data = "True"
            logging.info('Пароли не совпадают')
        else: return_data = "False"

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

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
                    host=localhost
                    dbname=postgres
                    user=postgres
                    password={os.getenv('PASSWORD_PG')}
                    port={os.getenv('PORT_PG')}
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
        logging.info("Пароль изменен")


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
    for i in range(4):
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

    logging.info('Пароль отправлен на почту')

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

def show_user_info(id):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from users WHERE id=$${id}$$")
        
        all_states = dict(cursor.fetchall()[0])
        logging.info('Инфа есть')
        return_data={}

        for key in all_states:
            if key != "password":
                return_data[key] = all_states[key]

        # счетчик статей
        cursor.execute(f"SELECT COUNT(*) from states WHERE id_u=$${id}$$")
        return_data['scnt'] = cursor.fetchone()[0]

        # счетчик вопросов
        cursor.execute(f"SELECT * from questions WHERE id_u=$${id}$$")
        return_data['qcnt'] = cursor.fetchone()[0]

        # счетчик ответов и комментариев
        cursor.execute(f"SELECT * from answers WHERE id_u=$${id}$$")
        cnt_a = cursor.fetchone()[0]
        cursor.execute(f"SELECT * from comments WHERE id_u=$${id}$$")
        cnt_c = cursor.fetchone()[0]
        return_data['acnt'] =cnt_a + cnt_c


    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
 

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Регистрация
@app.route('/registration', methods=['GET', 'POST'])
def user_registration():
    response_object = {'status': 'success'} #БаZа

    if request.method == 'POST':
        post_data = request.get_json()
        logging.info(add_user_todb(post_data.get('name'), post_data.get('email'), post_data.get('password'))) #Вызов фунции добавления пользователя в бд и ее debug

    return jsonify(response_object)

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
    response_object['all'] = show_user_info(request.args.get('id'))

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
        response_object['res'] = change_password(post_data.get('new_password'),post_data.get('old_passord'), "f527d19a-f56b-4614-bab6-63800ed79825")
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
        logging.info(send_code(post_data.get('email')))
    
    else:
        # ХЗ, вроде проверка кода подтверждения
        response_object['res'] = check_password(post_data.get('emailCode'), session.get('code'))
    
    return jsonify(response_object)
 

 # может ли юзер удалять/менять или нет
