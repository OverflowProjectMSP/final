from app import *


load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)
 
# Новый вопрос
def add_question(discriptions='', details='', dificulty='', tag='', id=''):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        send_question = []

        cursor.execute(f"SELECT COUNT(*) FROM question WHERE discriptions=$${discriptions}$$")  
        
        send_question.append(cursor.fetchone())
        # Существует ли такой же вопрос
        if send_question[0][0]==0:
            logging.info(details, 1)
            question_to_write = (uuid.uuid4().hex, discriptions, details, dificulty, tag, id)
            cursor.execute(f"INSERT INTO questions(id, discriptions, details, dificulty, tag, user_id) VALUES {question_to_write}")      
            pg.commit()
            
            
        return_data = "Вопрос добавлен"
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Отображение всех вапросов на frontend
def render_questions():
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from questions")

        all_questions = cursor.fetchall()  

        logging.info('Вопросы отображены')

        return_data = []

        for row in all_questions:
            return_data.append(dict(row))

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)

        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Добоволение статьи
def add_states(discriptions='', details='', id='', tag=''):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        logging.info(id)

        send_state = []

        cursor.execute(f"SELECT COUNT(*) FROM states WHERE discriptions=$${discriptions}$$")  
        send_state.append(cursor.fetchone())

        # Существует ли таккая же
        if send_state[0][0]==0:
            logging.info(details, 1)
            state_to_write = (uuid.uuid4().hex, discriptions, details,tag ,id)
            cursor.execute(f"INSERT INTO states(id, discriptions, details, tag, user_id) VALUES {state_to_write}")      
            pg.commit()
            
        logging.info('Статья добавлена')

        return_data = "Статья добавлена"
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Все вопросы/статьи от одного юзера
def show_all_by_user(id):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        logging.info(id)
        cursor.execute(f'SELECT * FROM questions WHERE user_=$${id}$$')
        questions = cursor.fetchall()
        cursor.execute(f'''SELEСT * FROM states
                                WHERE user_=$${id}$$''')
        
        states = cursor.fetchall()
        logging.info('Информация отпраленна')


        return_data = {
            'questions': questions,
            'states': states
        }

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# удалить что-то
def delete(id, isQ):
    if isQ:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f'''DELETE FROM questions WHERE id=$${id}$$''')

            pg.commit()
            return_data = 'ok'
            
        except (Exception, Error) as error:
            logging.error(f'DB: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data
    else:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
            logging.info(type(id))
            cursor.execute(f'''DELETE FROM states WHERE id=$${id}$$;''')

            pg.commit()
            return_data = 'ok'
        except (Exception, Error) as error:
            logging.error(f'DB: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data

# обновить что-то
def change(id, info, isQ):
    infor = info # без for
    if isQ:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)
        
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.excute(f'''UPDATE questions
                        SET (information)
                          WHEREE id=$${id}$$''')

            pg.commit()
            return_data = 'ok'
            
        except (Exception, Error) as error:
            logging.error(f'DB: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data
    else:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.excute(f'''UPDATE states
                        SET (information)
                          WHEREE id=$${id}$$''')
            pg.commit()
            return_data = 'ok'
        except (Exception, Error) as error:
            logging.error(f'DB: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data

# Вопросы форума    
def show_forum(filtre):
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''SELECT * FROM states WHERE tag=$${filtre}$$''')
        states = cursor.fetchall()
        cursor.execute(f'''SELECT * FROM questions WHERE tag=$${filtre}$$''')
        questions = cursor.fetchall()
        
        return_data = {
            "states": states,
            "questions": questions
        }

        logging.info(f'Вся информация о форуме {filtre} была отправлена')
        pg.commit()
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Отображение всех статей на frontend
def render_states():
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from states")
        
        all_states = cursor.fetchall()  
        logging.info('все статьи отображены')
        return_data = []

        for row in all_states:
            return_data.append(dict(row))

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
        
# Показываем что-то определенное
def show_one(id, isQ):
    if isQ:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f"SELECT * from states WHERE id = $${id}$$")
            
            all_states = cursor.fetchall()[0]
            
            all_asw = show_answers(True, id)


            return_data = {
                'question:': all_states,
                'answers': all_asw     
                           }

        except (Exception, Error) as error:
            logging.error(f'DB: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from states WHERE id = $${id}$$")
        
        all_states = cursor.fetchall()[0]

        all_asw = all_asw = show_answers(True, id)


        return_data = {
                'states': all_states,
                'answers': all_asw     
                           }

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
        
# ФИЛЬТРЫ
def filtre(filters, isQ):
    if not filters['filtr']:
        filtr = ''
    elif filters["filtr"]:
        filtr = ' WHERE'
        for i in filters:
            logging.info(i)
            if filters[i] != 'false':
                if i == 'filtr':
                    continue
                if filtr == ' WHERE':
                    filtr += f' {i}=$${filters[i]}$$'
                else:
                    filtr += f' AND {i}=$${filters[i]}$$'
    if isQ:
        try:
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor) 
            cursor.execute(f"SELECT * FROM questions{filtr}")
            result = cursor.fetchall()
            logging.info(f"SELECT * FROM questions{filtr}")
            return_data = []
            for row in result:
                return_data.append(dict(row))

        except (Exception, Error) as error:
            logging.info(f"Ошибка получения данных: {error}")
            return_data = 'Error'

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data
    else: 
        try:
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor) 
            cursor.execute(f"SELECT * FROM states{filtr}")
            result = cursor.fetchall()

            return_data = []
            for row in result:
                return_data.append(dict(row))

        except (Exception, Error) as error:
            logging.info(f"Ошибка получения данных: {error}")
            return_data = 'Error'

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data
            
def add_img( base, name, isAvatar, isQ,id):
    base=base[base.find(',')+1:]
    decoded_bytes = base64.b64decode(base)
    dote = name[name.find('.'):]
    if isAvatar:
        name = 'a_'+id+dote
        with open(os.path.join('/avatat/', name), "wb") as file:
            file.write(decoded_bytes)
        return 'http://127.0.0.1:5000/avatar/'+name
    
    if isQ:
        name = 'q_'+id+dote
        with open(os.path.join('/media/', name), "wb") as file:
                file.write(decoded_bytes)
        return 'http://127.0.0.1:5000/media/'+name
    
    name = 's_'+id+dote
    with open(os.path.join('/media/', name), "wb") as file:
            file.write(decoded_bytes)
    return 'http://127.0.0.1:5000/media/'+name

# Добовление ответа
def add_ans(text, isQ, idO, id_u):
    date = datetime.now().isoformat()
    to_write = (uuid.uuid4().hex, id_u, idO, text, date)   
    if isQ:
        obj = "answers(id, id_user, id_q, text, data)"
    else:
        obj = "comments(id, id_user, id_s, text, data)"

    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        print(f"INSERT INTO {obj} VALUES{to_write}")

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"INSERT INTO {obj} VALUES{to_write}")      
        print(1)
        pg.commit()  

        logging.info(to_write)

        return_data = "Комментарий добавлен!"

    except (Exception, Error) as error:
        logging.error(f"Ошибка добавления в базу данных: {error}")
        return_data = "Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

def show_answers(isQ, idO):
    if isQ:
        try:
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
            
            cursor.execute(f'''SELECT * FROM answers 
                       WHERE id_q = $${idO}$$
                       ORDER BY date''')
            
            return_data = cursor.fetchall()

            logging.info('Все ответы добавлены')

        except (Exception, Error) as error:
            logging.info(f"Ошибка получения данных: {error}")
            return_data = 'Error'

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''SELECT * FROM comments 
                       WHERE id_s = $${idO}$$
                       ORDER BY date''')
        
        return_data = cursor.fetchall()

        logging.info('Все комментарии добавлены')

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Новый вопрос
@app.route('/new-question', methods=['POST'])
def new_question(): 
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()
    post_data = post_data.get('form')
    logging.info(add_question(post_data.get('discriptions'), post_data.get('details'), post_data.get('dificulty'), post_data.get('tag'), session.get('id'))) #Вызов и debug функции добавления вопроса в бд
    
    return jsonify(response_object)

# Новая статья
@app.route('/new-state', methods=['GET', 'POST'])
def create_state(): 
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json().get('form')
    logging.info(1)
    logging.info(add_states(post_data.get('discriptions'), post_data.get('details'), session.get('id'), post_data.get('tag'))) #Вызов и debug функции добавления вопроса в бд
    
    return jsonify(responce_object)

#Страница со всеми вопросами
@app.route('/show-questions', methods=['GET'])
def show_questions():
    response_object = {'status': 'success'} #БаZа
    response_object['all'] = render_questions() #Вызов и возврат ответа на клиент функции для получения всех вопросов
    
    return jsonify(response_object)
 
# Фильтр статей
@app.route("/filtre-states", methods=['POST'])
def filtre_states():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json().get('body')
    logging.info(post_data)
    responce_object['all'] = filtre(post_data.get('filters'), False)

    return jsonify(responce_object)

# Фильтр вопросов
@app.route("/filtre-questions", methods=['POST'])
def filtre_questions():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json().get('body')
    logging.info(post_data)
    responce_object['all'] = filtre(post_data.get('filters'), True)

    return jsonify(responce_object)

# Вопросы форума
@app.route('/show-forum', methods=['GET'])
def show_f():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.args.get('language')


    responce_object['all'] = show_forum(post_data)

    return jsonify(responce_object)

# Одино что-то
@app.route('/show-one', methods=['GET'])
def one_something():
    responce_object = {'status': 'success'}

    # post_data = request.get_json()
    id = request.args.get('id')
    is_Q = request.args.get('q')

    if is_Q:
        responce_object['all'] = show_one(id, True)
    else:
        responce_object['all'] = show_one(id, False)


    return jsonify(responce_object)

# Удаление чего-то
@app.route('/delete',methods=['DELETE'])
def delete_():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.args.get('id')

    if  request.args.get('q') == 'true':
        responce_object['all'] = delete(post_data, True) 
    else:
        responce_object['all'] = delete(post_data, False) 
    
    logging.info(responce_object['all'])

    return jsonify(responce_object)

# Изменение чего-то
@app.route('/change',methods=['PUT'])
def change_():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json()

    if post_data.get('question'):
        responce_object['all'] = change(post_data.get('id'), post_data.get('all'), True) # а что - решим потом (название поменять надо)
    else: 
        responce_object['all'] = change(post_data.get('id'), post_data.get('all'), False) # а что - решим потом (название поменять надо)

    logging.info(responce_object['all'])

    return jsonify(responce_object)

#Страница со всеми статьями
@app.route('/show-states', methods=['GET'])
def show_sates():
    response_object = {'status': 'success'} #БаZа

    response_object['all'] = render_states() #Вызов и возврат ответа на клиент функции для получения всех вопросов
    
    return jsonify(response_object)

# все от одного юзера
@app.route('/show-all-by-user', methods=['GET'])
def show_all_by_user_route():
    response_object = {'status': 'success'} #БаZа

    post_data = request.args.get('id')

    response_object['all'] = show_all_by_user(post_data)

    logging.info('Отправлено')
    return jsonify(response_object)
 
@app.route('/answers', methods=['POST', 'GET'])
def add_a():
    if request.method == "POST":

        response_object = {'status': 'success'} #БаZа

        post_data = request.get_json()
        text = post_data.get('text')

        if post_data.get('q'):
            response_object['all'] =  add_ans(text, True, post_data.get('id'), session.get('id'))
            return jsonify(response_object)
        response_object['all'] =  add_ans(text, False, post_data.get('id'), session.get('id'))
        return jsonify(response_object)

    # response_object['res'] = 