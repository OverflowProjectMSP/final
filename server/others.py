from app import * 


load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("others.py have connected")

# Добавление сообщения в бд (чат форума)
def chat(id, time, msg):
    try: 
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        message_id = uuid.uuid4().hex # Записываем id сообщения в отдельную переменную для отпраки на клиент

        message_to_write = (message_id, id, time, msg)
        cursor.execute(f"INSERT INTO messages(message_id, user_id, time, msg) VALUES {message_to_write}")
        pg.commit()

        logging.info('Сообщение добавлено')

        return_data = message_id

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
 
def show_avatar(id):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''SELECT avatar FROM users
                      WHERE id = $${id}$$''')
        
        link = cursor.fetchall()[0]

        logging.info(f'Аватар юзере {id} отображен')
        
        if link == [None]:
            return_data = 'No'
        else: return_data = link
    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'No'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

def helper(phone, email, msg, id_u):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"INSERT INTO helper VALUES('{uuid.uuid4().hex}', '{msg}', '{phone}', '{email}', '{id_u}')")
        
        pg.commit()

        logging.info(f"Добавлен в helper '{msg}', '{phone}', '{email}', '{id_u}' ")

        return 'Ваня'
    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Errro'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

def is_solved(id, isS):
    try: 
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        cursor.execute(f"UPDATE questions SET is_solved=$${isS}$$ WHERE id=$${id}$$")
        pg.commit()

        logging.info('Информаация о решенности вопроса обновлена')
        return_data = 'ok'

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Errro'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
    
def count_reg():
    try: 
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute('''SELECT COUNT(*) FROM users''')

        return_data = cursor.fetchall()[0]

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Errro'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Чат форума
@app.route('/chat', methods=['POST', 'PUT'])
def chat_forum():
    responce_object = {'status' : 'success'} #БаZа
    post_data = request.get_json()

    if request.method == 'PUT': # Обновка вопроса
        pass
    else: 
        responce_object['id_question'] = chat(session.get('id'), datetime.now(), post_data.get('msg')) #   Возвращает id сообщения и добовляет его в бд (сообщение)       
    
    return jsonify(responce_object)
  
# проверка может ли юзер исправлять что-то
@app.route('/check', methods=['GET'])
def check():
    response_object = {'status': 'success'} #БаZа
    id = request.args.get('id')

    if id == session.get('id'):
        response_object['isEdit'] = 'true'
        logging.info(f'Пользователь {id} может внести изменения')
    else:
        response_object['isEdit'] = 'false'
        logging.info(f'Пользователь {id} не может вносить изменения')

    return  jsonify(response_object)
 
@app.route('/avatar', methods=['GET'])
def ava():
    response_object = {'status': 'success'} #БаZа

    response_object['link'] = show_avatar(session.get('id'))

    return jsonify(response_object)

@app.route('/avatar/<path:filename>')
def serve_file(filename):
    path = filename
    print(AVATAR+path)
    # if not os.path.exists('{}/{}'.format('avatar/', filename)):
    #     logging.info({'error': 'File not found'}, 404)
    #     return jsonify({'error': 'File not found'}), 404

    return send_from_directory(directory='avatar/', path=path)

@app.route('/session', methods=['GET'])
def session_(): 
    return jsonify({'status': 'success', 'id': session.get('id')})
 
@app.route('/help', methods=['POST'])
def help_():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json()

    responce_object['all'] = helper(post_data.get('phone'), post_data.get('email'), post_data.get('message'), session.get('id'))

    return  jsonify(responce_object)

@app.route('/avatarka', methods=['GET'])
def ava_():
    response_object = {'status': 'success'} #БаZа

    response_object['link'] = show_avatar(session.get('id'))

    return jsonify(response_object)

@app.route('/check-r', methods=['GET'])
def session__():
    if 'id' in session: 
        logging.info('Пользователь зашел в аккаунт')
        return jsonify({'status': 'success', 'all': 'true'})
    else: 
        logging.info('Пользователь не зашел в аккаунт')
        return jsonify({'status': 'success', 'all': 'false'})

@app.route('/is-solved', methods=['PUT'])
def is_s():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    is_solved(post_data.get('id'), post_data.get('is_solved'))
    return  jsonify(response_object) 

@app.route('/users-reg', methods=['GET'])
def reg_():
    responce_object = {'status': 'success'} #БаZа

    responce_object['regs'] = count_reg()[0]

    return jsonify(responce_object)
