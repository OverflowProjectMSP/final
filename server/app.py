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

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

PASSWORD_PG = os.getenv('PASSWORD_PG')
PORT_PG = os.getenv('PORT_PG')
USER_PG = os.getenv('USER_PG')
HOST_PG = os.getenv('HOST_PG')
SECRET_KEY = os.getenv('SERCRET_KEY')

app = Flask(__name__)

app.secret_key = SECRET_KEY
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 * 24
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
# app.config["SESSION_COOKIE_SECURE"] = "None"
app.config.update(
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_HTTPONLY=True
)

# enable CORS
CORS(app, resources={r"*": {"origins": "http://localhost:5173", 'supports_credentials': True}})

#Главная страница
@app.route('/', methods=['GET'])
def home():

    response_object = {'status': 'success'} #БаZа
    response_object['message'] = session.get('id')
    logging.warning('1')
    logging.info(session.get('id')) #debug
    logging.warning(response_object)
    session.pop('id', None)
    return jsonify(response_object)

def add_tables():
    try:
        pg = psycopg2.connect(f"""
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"""create table if not exists users(
                        id uuid,
                        username text,
                        email text,
                        password text,
                        name text,
                        surname text,
                        interestings text,
                        about text,
                        country text,
                        region text,
                        city text,
                        telegram text,
                        skype text,
                        discord text,
                        facebook text,
                        phonenumber text,
                        github text,
                        avatar text,
                        admin bool,
                    )""")
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS questions(
                    id uuid,
                    descriptions text,
                    details text,
                    dificulty text,
                    tag text,
                    id_u uuid,
                    data timestamp,
                    is_solved bool
                )""")
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS states(
                    id uuid,
                    descriptions text,
                    details text,
                    tag text,   
                    id_u uuid,
                    data timestamp
                )""")
        cursor.execute(f"""create table if not exists answers(
                    id text,
                    id_u text, 
                    id_q text,
                    text text,
                    data timestamp
                )""")
        cursor.execute(f"""create table if not exists comments(
                    id text,
                    id_u text, 
                    id_s text,
                    text text,
                    data timestamp
                )""")
        cursor.execute(f"""create table if not exists helper(
                id uuid,
                msg text,
                phone text,
                email text,
                id_u uuid
            )""")

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
    

    

from user import * 
from render_and_adding import *
from others import * 

if __name__ == '__main__':
    app.run(debug=True)


