from app import *


load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)
 
logging.info("render_and_adding.py have connected")



# Новый вопрос
def add_question(discriptions='', details='', dificulty='', tag='', id=''):
    try: 
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        send_question = []

        cursor.execute(f"SELECT COUNT(*) FROM questions WHERE descriptions=$${discriptions}$$")  
        
        send_question.append(cursor.fetchone())
        # Существует ли такой же вопрос
        if send_question[0][0]==0:
            logging.info(details, 1)
            question_to_write = (uuid.uuid4().hex, discriptions, details, dificulty, tag, id, datetime.now().isoformat(), True)
            cursor.execute(f"INSERT INTO questions(id, descriptions, details, dificulty, tag, id_u, data, is_solved) VALUES {question_to_write}")   
            # print(f"INSERT INTO questions(id, descriptions, details, dificulty, tag, id_u, data) VALUES {question_to_write}")   
            pg.commit()
            return_data = "Вопрос добавлен"
        else : return_data = "Уже существует"
            
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        
        return_data = f"Error" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info(return_data)
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Отображение всех вапросов на frontend
def render_questions():
    try: 
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from questions")

        all_questions = cursor.fetchall()  

        logging.info('Вопросы отображены')

        return_data = []

        for row in all_questions:
            a = dict(row)
            cursor.execute(f"SELECT COUNT(*) from answers WHERE id_q=$${a['id']}$$")
            a['acnt'] = cursor.fetchone()[0]
            return_data.append(a)

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)

        return_data = f"Error" 

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
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        logging.info(id)

        send_state = []

        cursor.execute(f"SELECT COUNT(*) FROM states WHERE descriptions=$${discriptions}$$")  
        send_state.append(cursor.fetchone())

        # Существует ли таккая же
        if send_state[0][0]==0:
            logging.info(details, 1)
            state_to_write = (uuid.uuid4().hex, discriptions, details,tag, id, datetime.now().isoformat())
            cursor.execute(f"INSERT INTO states(id, descriptions, details, tag, id_u, data) VALUES {state_to_write}")
            pg.commit()
            return_data = "Статья добавлена"
        else: return_data = 'Такая статья уже есть'
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info(return_data)
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Все вопросы/статьи от одного юзера
def show_all_by_user(id):
    try: 
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        logging.info(id)
        cursor.execute(f'SELECT * FROM questions WHERE id_u=$${id}$$')
        questions = cursor.fetchall()
        q = []
        for row in questions:
            q.append(dict(row))

        cursor.execute(f'SELECT * FROM states WHERE id_u=$${id}$$')
        states = cursor.fetchall()

        s = []
        for row in states:
            s.append(dict(row))
        logging.info('Информация отпраленна')


        return_data = {
            'questions': q,
            'states': s
        }

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error" 

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
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f'''DELETE FROM questions WHERE id=$${id}$$''')
            cursor.execute(f'''DELETE FROM answers WHERE id_q=$${id}$$''')

            pg.commit()
            return_data = 'ok'
            logging.info(f'Вопрос {id} удален')
        except (Exception, Error) as error:
            logging.error(f'DB: ', error)
            return_data = f"Error" 

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data

    try: 
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        logging.info(type(id))
        cursor.execute(f'''DELETE FROM states WHERE id=$${id}$$;''')
        cursor.execute(f'''DELETE FROM comments WHERE id_s=$${id}$$;''')

        pg.commit()
        return_data = 'Ok'
        logging.info(f'Статья {id} удалена')

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error" 

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# обновить что-то
def change(id, info, isQ):
    infor = ''
    for i in info:
        print(i)
        if info[i] != 'false':
            if i == 'data':
                infor += f' {i}=$${datetime.now().isoformat()}$$'
            elif infor == '':
                infor += f' {i}=$${info[i]}$$'
            else:
                infor += f', {i}=$${info[i]}$$'
    if isQ:
        try: 
            pg = psycopg2.connect(f"""
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f'''UPDATE questions
                        SET {infor}
                        WHERE id=$${id}$$''')

            pg.commit()
            return_data = 'ok'
            logging.info(f'Вопрос {id} изменен')
            
        except (Exception, Error) as error:
            logging.error(f'DB: ', error)
            return_data = f"Error" 

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data

    try: 
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''UPDATE states
                    SET {info}
                    WHERE id=$${id}$$''')
        pg.commit()
        return_data = 'ok'
        logging.info(f'Стаья {id} изменена')

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error" 

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
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''SELECT * FROM states WHERE tag=$${filtre}$$''')
        states = cursor.fetchall()
        cursor.execute(f'''SELECT * FROM questions WHERE tag=$${filtre}$$''')
        questions = cursor.fetchall()

        q = []
        for row in questions:
            q.append(dict(row))

        s = []
        for row in states:
            s.append(dict(row))
        return_data = {
            "states": s,
            "questions": q
        }

        logging.info(f'Вся информация о форуме {filtre} была отправлена')
        pg.commit()
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error" 

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
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from states")
        
        all_states = cursor.fetchall()  
        return_data = []

        for row in all_states:
            a = dict(row)
            cursor.execute(f"SELECT COUNT(*) from comments WHERE id_s=$${a['id']}$$")
            a['acnt'] = cursor.fetchone()[0]
            return_data.append(a)

        logging.info('все статьи отображены')
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error" 

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
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f"SELECT * from questions WHERE id = $${id}$$")
            # print(cursor.fetchall())
            
            all_q = dict(cursor.fetchall()[0])
            
            all_asw = show_answers(True, id)
            

            return_data = {
                'question': all_q,
                'answers': all_asw     
                           }
            logging.info(f'Вопрос {id} был отправлен')

        except (Exception, Error) as error:
            logging.error(f'DB: ', error)
            return_data = f"Error" 

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data
    try: 
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        print(id)
        cursor.execute(f"SELECT * from states WHERE id = $${id}$$")
        
        all_states = dict(cursor.fetchall()[0])

        all_asw = show_answers(False, id)


        return_data = {
                'states': all_states,                        
                'answers': all_asw     
                           }                           
        logging.info(f'Сатья {id} была отправлен')
                                                        
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error" 

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
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor) 
            cursor.execute(f"SELECT * FROM questions{filtr}")
            result = cursor.fetchall()
            return_data = []
            for row in result:
                return_data.append(dict(row))

            logging.info(f'Вся информация о вопросах с фильрами {filtre} была отправлена')

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
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor) 
        cursor.execute(f"SELECT * FROM states{filtr}")
        result = cursor.fetchall()

        return_data = []
        for row in result:
            return_data.append(dict(row))

        logging.info(f'Вся информация о стаьях с фильрами {filtre} была отправлена')

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
        with open(os.path.join('avatar/', name), "wb") as file:
            file.write(decoded_bytes)
        return 'http://127.0.0.1:5000/avatar/'+name
    
    if isQ:
        name = 'q_'+id+dote
        with open(os.path.join('media/', name), "wb") as file:
                file.write(decoded_bytes)
        return 'http://127.0.0.1:5000/media/'+name
    
    name = 's_'+id+dote
    with open(os.path.join('media/', name), "wb") as file:
            file.write(decoded_bytes)
    return 'http://127.0.0.1:5000/media/'+name

# Добовление ответа
def add_ans(text, isQ, idO, id_u):
    date = datetime.now().isoformat()
    to_write = (uuid.uuid4().hex, id_u, idO, text, date)   
    if isQ:
        obj = "answers(id, id_u, id_q, text, data)"
    else:
        obj = "comments(id, id_u, id_s, text, data)"

    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        print(f"INSERT INTO {obj} VALUES{to_write}")

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"INSERT INTO {obj} VALUES{to_write}")      

        pg.commit()  

        logging.info(to_write)

        return_data = "Комментариии отправлены"

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
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
            
            cursor.execute(f'''SELECT * FROM answers 
                       WHERE id_q = $${idO}$$
                       ORDER BY data''')
            
            data_ = cursor.fetchall()
            return_data = []
            for row in data_:
                return_data.append(dict(row))

            logging.info('Все ответы показаны')

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
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''SELECT * FROM comments 
                       WHERE id_s = $${idO}$$
                       ORDER BY data''')
        
        data = cursor.fetchall()
        print(f'''SELECT * FROM comments 
                       WHERE id_s = $${idO}$$
                       ORDER BY data''')
        return_data = []
        for row in data:
            return_data.append(dict(row))

        logging.info('Все комментарии отправлены')

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

# Отображение всех статей на frontend
def filtre_states(fil):
    status = 0
    filtrs = ''
    for i in fil:
        if fil[i] != '':
            print(i)
            if filtrs!='':
                if i!='name' and i!='descriptions':
                    filtrs+=f' and {i}=$${fil[i]}$$'
            else:
                if i!='name' and i!='descriptions':
                    filtrs+=f'{i}=$${fil[i]}$$'
    if filtrs != '' or fil['name'] != '':
        try: 
            pg = psycopg2.connect(f"""
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
            ids = []
            if fil['name'] != '': 
                cursor.execute(f'''select id from users where username like '%{fil["name"]}%' ''')
                ids = cursor.fetchall()
                ors = '('
                for i in ids:
                    if ors !='(': ors+=f' or id_u=$${i[0]}$$'
                    else: ors+=f'id_u=$${i[0]}$$'
                ors+=')'
            else: ors = ''
            if filtrs == '' and ids != []: cursor.execute(f'''select * from states where descriptions like '%{fil["descriptions"]}%' and {ors}''')
            elif ids != []: cursor.execute(f'''select * from states where descriptions like '%{fil["descriptions"]}%' and {filtrs} and {ors}''')
            else: 
                status = 1
                return []
            # print(f'''select * from states where descriptions like '%{fil["descriptions"]}%' and {filtrs} and {ors}''')
            q = cursor.fetchall()
            return_data = []
            for row in q:
                return_data.append(dict(row))

        except (Exception, Error) as error:
            logging.error(f'DB: ', error)

            return_data = f"Error" 

        finally:
            if pg and status == 0:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data
    else:
        try: 
            pg = psycopg2.connect(f"""
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute('''select * from states''')
            q = cursor.fetchall()
            return_data = []
            for row in q:
                return_data.append(dict(row))
        

        except (Exception, Error) as error:
            logging.error(f'DB: ', error)

            return_data = f"Error" 

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data

# Отображение всех вапросов на frontend
def filtre_question(fil):
    status = 0
    filtrs = ''
    for i in fil:
        if fil[i] != '':
            print(i)
            if filtrs!='':
                if i!='name' and i!='descriptions':
                    filtrs+=f' and {i}=$${fil[i]}$$'
            else:
                if i!='name' and i!='descriptions':
                    filtrs+=f'{i}=$${fil[i]}$$'
    if (filtrs != '' or fil['name'] != '') or fil['descriptions'] != '':
        try: 
            pg = psycopg2.connect(f"""
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
            ids = []
            if fil['name'] != '': 
                cursor.execute(f'''select id from users where username like '%{fil["name"]}%' ''')
                ids = cursor.fetchall()
                ors = '('
                for i in ids:
                    if ors !='(': ors+=f' or id_u=$${i[0]}$$'
                    else: ors+=f'id_u=$${i[0]}$$'
                ors+=')'
            else: ors = ''
            print(filtrs, ids)
            if filtrs == '' and ids != []: cursor.execute(f'''select * from questions where descriptions like '%{fil["descriptions"]}%' and {ors}''')
            elif ids != []: cursor.execute(f'''select * from questions where descriptions like '%{fil["descriptions"]}%' and {filtrs} and {ors}''')
            elif ids == [] and filtrs != '': cursor.execute(f'''select * from questions where descriptions like '%{fil["descriptions"]}%' and {filtrs}''')
            elif fil['descriptions'] != '' and filtrs != '': cursor.execute(f'''select * from questions where descriptions like '%{fil["descriptions"]}%' and {filtrs}''')
            elif fil['descriptions'] != '': cursor.execute(f'''select * from questions where descriptions like '%{fil["descriptions"]}%' ''')
            else: 
                status = 1
                return []
            # print(f'''select * from states where descriptions like '%{fil["descriptions"]}%' and {filtrs} and {ors}''')
            q = cursor.fetchall()
            return_data = []
            for row in q:
                return_data.append(dict(row))

        except (Exception, Error) as error:
            logging.error(f'DB: ', error)

            return_data = f"Error" 

        finally:
            if pg and status == 0:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
                return return_data
    else:
        try: 
            pg = psycopg2.connect(f"""
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute('''select * from questions''')
            q = cursor.fetchall()
            return_data = []
            for row in q:
                return_data.append(dict(row))
        

        except (Exception, Error) as error:
            logging.error(f'DB: ', error)

            return_data = f"Error" 

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
    response_object['res'] = add_question(post_data.get('descriptions'), post_data.get('details'), post_data.get('dificulty'), post_data.get('tag'), session.get('id')) #Вызов и debug функции добавления вопроса в бд
    
    return jsonify(response_object)

# Новая статья
@app.route('/new-state', methods=['GET', 'POST'])
def create_state(): 
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json().get('form')
    logging.info(1)
    responce_object['res'] = add_states(post_data.get('descriptions'), post_data.get('details'), session.get('id'), post_data.get('tag')) #Вызов и debug функции добавления вопроса в бд
    
    return jsonify(responce_object)

#Страница со всеми вопросами
@app.route('/show-questions', methods=['GET'])
def show_questions():
    response_object = {'status': 'success'} #БаZа
    response_object['all'] = render_questions() #Вызов и возврат ответа на клиент функции для получения всех вопросов
    
    return jsonify(response_object)
 
# Фильтр статей
@app.route("/filtre-states", methods=['GET'])
def filtre_states_():
    responce_object = {'status' : 'success'} #БаZа

    
    filtrs = {
        'descriptions': request.args.get('title'),
        'name': request.args.get('author'),
        'tag': request.args.get('tag'),
    }
    responce_object['all'] = filtre_states(filtrs)

    return jsonify(responce_object)

# Фильтр вопросов
@app.route("/filtre-questions", methods=['GET'])
def filtre_questions_():
    responce_object = {'status' : 'success'} #БаZа

    filtrs = {
        'descriptions': request.args.get('title'),
        'name': request.args.get('author'),
        'tag': request.args.get('tag'),
        'dificulty': request.args.get('dificulty'),
    }
    responce_object['all'] = filtre_question(filtrs)

    return jsonify(responce_object)

# Вопросы форума
@app.route('/show-forum', methods=['GET'])
def show_f():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.args.get('tag')
    print(post_data)

    responce_object['all'] = show_forum(post_data)

    return jsonify(responce_object)

# Одино что-то
@app.route('/show-one', methods=['GET'])
def one_something():
    responce_object = {'status': 'success'}

    # post_data = request.get_json()
    id = request.args.get('id')
    is_Q = request.args.get('q')
    print(is_Q)
    if is_Q == 'true':
        responce_object['all'] = show_one(id, True)
    else:
        print(1)
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

    if post_data.get('q') == "true":
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
 
@app.route('/answers', methods=['POST'])
def add_a():

    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()
    text = post_data.get('text')

    if post_data.get('q') == 'true':
        response_object['all'] =  add_ans(text, True, post_data.get('id'), session.get('id'))
        return jsonify(response_object)
    response_object['all'] =  add_ans(text, False, post_data.get('id'), session.get('id'))
    return jsonify(response_object)