# =====Irrigação Inteligente=====
# Projeto desenvolvido por alunos da disciplina Sitemas Distribuídos
# ministrada pelo docente Sérgio Ribeiro.

# ====INSTALAÇÕES====
# pip install pyzmq   : ZeroMQ
# pip install fastapi : FastAPI (framework utilizado para criação de APIs)
# pip install uvicorn : servidor web para Python - utilizado pelo FastAPI.
# Para iniciar o servidor : python -m uvicorn subscriber:app --reload

# =====SUBSCRIBER=====
# Responsável pelo recebimento de dados provindos do ESP32 e também
# pela disponibização de endpoints para que seja realizada a integração
# Telegram - Servidor.


import zmq
import json
from fastapi import FastAPI, Response
from pydantic import BaseModel
import uvicorn
import threading
import sqlite3

app = FastAPI()

base_url = "192.168.100.22"
statusPort = "2020"
paramsPort = "2021"
urlStatus = f"tcp://{base_url}:{statusPort}"
urlParams = f"tcp://{base_url}:{paramsPort}"


class Request(BaseModel):
    tipo_cultura: int


class Status(BaseModel):
    umidade: int


def receive_status(last_umidade=0):
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect(urlStatus)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"status")

    poller = zmq.Poller()
    poller.register(subscriber, zmq.POLLIN)

    try:
        socks = dict(poller.poll(1000))
    except KeyboardInterrupt:
        subscriber.close()
        context.term()
        exit()

    if subscriber in socks:
        [address, contents] = subscriber.recv_multipart()
        conteudo = json.loads(contents)
        umidade = conteudo['umidade']

        if umidade != last_umidade:
            if umidade != None:
                update_status(umidade)
            last_umidade = umidade

        subscriber.close()
        context.term()
        return umidade


def run_subscriber():
    last_umidade = 0
    while True:
        last_umidade = receive_status(last_umidade)


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
    cursor = conn.execute('SELECT cod FROM status WHERE cod = 1')
    retorno = cursor.fetchone()
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
    read_status()

    subscriber_thread = threading.Thread(target=run_subscriber)
    server_thread = threading.Thread(target=run_server)

    subscriber_thread.start()
    server_thread.start()

    subscriber_thread.join()
    server_thread.join()


@app.get("/")
def getData():
    umidade = receive_status()
    response_dict = {"umidade": umidade}
    return Response(content=json.dumps(response_dict), media_type="application/json")


@app.post("/")
def postData(request: Request):
    update_cultura(request.tipo_cultura)
    # TODO: fazer a regra de negócio e a chamada no endpoint do ESP32 que irá settar o tipo de cultura
    return request


if __name__ == "__main__":
    main()
