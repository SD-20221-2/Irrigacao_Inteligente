# from enum import Enum
import json
from fastapi import FastAPI, Response
from pydantic import BaseModel
import uvicorn
import threading
import sqlite3
import paho.mqtt.client as mqtt

app = FastAPI()

base_url = "192.168.100.22"
statusPort = "2020"
urlStatus = f"mqtt://{base_url}:{statusPort}"
mqtt_server = "localhost"
mqtt_port = 1883


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
        update_status(umidade)


def run_subscriber():
    client = mqtt.Client()
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
                    umidade INTEGER NOT NULL)
                ''')

    cursor = conn.execute('SELECT cod FROM status WHERE cod = 1')

    if cursor.fetchone() == None:
        conn.execute(
            '''INSERT INTO status (cod, umidade) VALUES (1, 0)''')

    conn.commit()
    conn.close()


def read_status():
    conn = sqlite3.connect('irrigacao_inteligente.db')
    cursor = conn.execute('SELECT umidade FROM status WHERE cod = 1')
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


def update_status(umidade):
    conn = sqlite3.connect('irrigacao_inteligente.db')
    conn.execute(f"UPDATE status SET umidade = {umidade} WHERE cod = 1")
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


@app.get("/stats")
def getData():
    umidade = read_status()
    response_dict = {"umidade": umidade}
    return Response(content=json.dumps(response_dict), media_type="application/json")


@app.get("/params")
def getParams():
    tipo_cultura = read_params()
    response_dict = {"codCultura": tipo_cultura}
    return Response(content=json.dumps(response_dict), media_type="application/json")


@app.post("/stats")
def postData(request: Request):
    update_cultura(request.tipo_cultura)
    return request


if __name__ == "__main__":
    main()
