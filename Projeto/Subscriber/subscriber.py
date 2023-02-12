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
from fastapi import FastAPI

app = FastAPI()

base_url = "192.168.100.22"
port = "2020"
url = "tcp://" + base_url + ":" + port


def recuperar_dados():
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect(url)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"umidade")

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
        subscriber.close()
        context.term()
        return conteudo


@app.get("/")
def getRegarOuNao():
    return recuperar_dados()
