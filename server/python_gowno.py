from app import *
from tg import *
from render_and_adding import *

import requests as req


load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("python_govno.py have connected")


@app.route("/delete-ans", methods=["DELETE"])
def delete_ans_b():
    response_object = {'status': 'success'} #БаZа

    post_data = request.args
    idO = post_data.get('id')
    if post_data.get("isQ") == "true":
        if is_can_edit(idO, True, session.get("id")) or check_is_admin(session.get("id")):
            response_object["res"] = delete_ans(idO, True)
    elif is_can_edit(idO, False, session.get("id")) or check_is_admin(session.get("id")):
        response_object["res"] = delete_ans(idO, False)
    return jsonify(response_object)


def delete_ans(id, isQ):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if isQ:
            cursor.execute(f"DELETE FROM answers WHERE id=$${id}$$")
        else:
            cursor.execute(f"DELETE FROM comments WHERE id=$${id}$$")

        pg.commit()
        return_data="ok"
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


def is_can_edit(idO: str, isQ: bool, id_u: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if isQ:
            cursor.execute(f"SELECT id_u FROM answers WHERE id=$${idO}$$")
            return_data = cursor.fetchone()[0] == id_u
        else:
            cursor.execute(f"SELECT id_u FROM comments WHERE id=$${idO}$$")
            logging.info(id_u)
            logging.info(cursor.fetchone()[0])
            logging.info(cursor.fetchone()[0] == id_u)
            return_data = cursor.fetchone()[0] == id_u

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


