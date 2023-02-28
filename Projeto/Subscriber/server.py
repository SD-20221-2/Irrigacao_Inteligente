# from enum import Enum
import json
from fastapi import FastAPI, Response
from pydantic import BaseModel
import uvicorn
import threading
import sqlite3
import paho.mqtt.client as mqtt

app = FastAPI()

# mqtt_server = "l828da7e.ala.us-east-1.emqxsl.com"
# mqtt_server = "broker.emqx.io"
# tcp://0.tcp.sa.ngrok.io:11272
mqtt_server = "0.tcp.sa.ngrok.io"
mqtt_port = 11272
username = "irrigacao"
password = "senha123"


class Request(BaseModel):
    tipo_cultura: int


class Status(BaseModel):
    umidade: int


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("status")


def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    if msg.topic == "status":
        conteudo = json.loads(msg.payload)
        umidade = conteudo['umidade']
        precisaRegar = conteudo['precisaRegar']
        # print("new message: umidade: " + str(umidade) +
        #       "%, precisaRegar: " + str(precisaRegar))
        update_status(umidade, precisaRegar)


def run_subscriber():
    client = mqtt.Client("2")
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqtt_server, mqtt_port, 60)
    client.loop_forever()


def run_server():
    uvicorn.run(app, host="localhost", port=8002)


def create_or_connect_server():
    conn = sqlite3.connect('irrigacao_inteligente.db')

    conn.execute('''CREATE TABLE IF NOT EXISTS cultura
                    (cod INTEGER PRIMARY KEY,
                    tipo_cultura INTEGER NOT NULL)
                ''')

    cursor = conn.execute('SELECT cod FROM cultura WHERE cod = 1')

    if cursor.fetchone() == None:
        conn.execute(
            '''INSERT INTO cultura (cod, tipo_cultura) VALUES (1, 0)''')

    conn.execute('''CREATE TABLE IF NOT EXISTS status
                    (cod INTEGER PRIMARY KEY,
                    umidade INTEGER NOT NULL,
                    precisa_regar INTEGER NOT NULL)
                ''')

    cursor = conn.execute('SELECT cod FROM status WHERE cod = 1')

    if cursor.fetchone() == None:
        conn.execute(
            '''INSERT INTO status (cod, umidade, precisa_regar) VALUES (1, 0, 0)''')

    conn.commit()
    conn.close()


def read_status(param):
    conn = sqlite3.connect('irrigacao_inteligente.db')
    if param == "umidade":
        cursor = conn.execute('SELECT umidade FROM status WHERE cod = 1')
    if param == "precisaRegar":
        cursor = conn.execute('SELECT precisa_regar FROM status WHERE cod = 1')
    retorno = cursor.fetchone()[0]
    conn.close()
    return retorno


def read_params():
    conn = sqlite3.connect('irrigacao_inteligente.db')
    cursor = conn.execute('SELECT tipo_cultura FROM cultura WHERE cod = 1')
    retorno = cursor.fetchone()[0]
    conn.close()
    return retorno


def update_cultura(cultura):
    conn = sqlite3.connect('irrigacao_inteligente.db')
    conn.execute(f"UPDATE cultura SET tipo_cultura = {cultura} WHERE cod = 1")
    conn.commit()
    conn.close()


def update_status(umidade, precisaRegar):
    conn = sqlite3.connect('irrigacao_inteligente.db')
    conn.execute(f"UPDATE status SET umidade = {umidade} WHERE cod = 1")
    conn.commit()
    conn.execute(
        f"UPDATE status SET precisa_regar = {precisaRegar} WHERE cod = 1")
    conn.commit()
    conn.close()


def main():
    create_or_connect_server()

    subscriber_thread = threading.Thread(target=run_subscriber)
    server_thread = threading.Thread(target=run_server)

    subscriber_thread.start()
    server_thread.start()

    subscriber_thread.join()
    server_thread.join()


@app.get("/status")
def getData():
    umidade = read_status('umidade')
    precisaRegar = read_status('precisaRegar')
    response_dict = {"umidade": umidade, "precisaRegar": precisaRegar}
    return Response(content=json.dumps(response_dict), media_type="application/json")


@app.get("/params")
def getParams():
    tipo_cultura = read_params()
    response_dict = {"codCultura": tipo_cultura}
    return Response(content=json.dumps(response_dict), media_type="application/json")


@app.post("/params")
def postData(request: Request):
    update_cultura(request.tipo_cultura)
    return request


if __name__ == "__main__":
    main()
