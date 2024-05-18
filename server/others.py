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
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
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
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''SELECT avatar FROM users
                      WHERE id = $${id}$$''')
        
        link = cursor.fetchall()[0]

        
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
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"INSERT INTO helper VALUES('{uuid.uuid4().hex}', '{msg}', '{phone}', '{email}', '{id_u}')")
        
        pg.commit()

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

# показ id avtar name
def show_not_all(id):
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''SELECT id, name, avatr FROM users
                      WHERE id = $${id}$$''')
        
        info = dict(cursor.fetchall()[0])
        return_data = {}
        for key in info:
            return_data[key] = info[key]

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'No'

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

# # может ли юзер удалять/менять или нет
# @app.route('/check-user',methods=['GET'])
# def check_user():
#     responce_object = {'status' : 'success'} #БаZа

#     post_data = request.get_json()

#     if  post_data.get('id')==session.get('id'):
#         responce_object['user'] = "True"
#     else: 
#         responce_object['user'] = "False"

#     return jsonify(responce_object)
  
# проверка может ли юзер исправлять что-то
@app.route('/check', methods=['GET'])
def check():
    response_object = {'status': 'success'} #БаZа
    id = request.args.get('id')

    logging.info(id)

    if id == session.get('id'):
        response_object['isEdit'] = 'true'

    else:
        response_object['isEdit'] = 'false'

    return  jsonify(response_object)
 
@app.route('/avatar', methods=['GET'])
def ava():
    response_object = {'status': 'success'} #БаZа

    response_object['link'] = show_avatar(session.get('id'))

    print(response_object)
    return jsonify(response_object)

@app.route('/avatr/<path:filename>')
def serve_file(filename):
    path = filename
    print('/avatar/'+path)
    if not os.path.exists('{}/{}'.format('/avatar/', '/'+filename)):
        return jsonify({'error': 'File not found'}), 404

    return send_from_directory(directory='/avatar/', path=path)

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
    if 'id' in session: return jsonify({'status': 'success', 'all': 'true'})
    else: return jsonify({'status': 'success', 'all': 'false'})

