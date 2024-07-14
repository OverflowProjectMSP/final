from app import *

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("tg.py have connected")


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

@app.route('/auth-tg', methods=["POST"])
def auth_tg_():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    response_object['res'], chat_id = auth_tg(post_data.get("hash_id"), session.get("id"))
    if chat_id!=-1 and response_object['res'] != "Err":
        response_object["res"] = tg_sendMessage(chat_id, "Поздравляю с успешной ауентифкацией на сайте")
    return jsonify(response_object)