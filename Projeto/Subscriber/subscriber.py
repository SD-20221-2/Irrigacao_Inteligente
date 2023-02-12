# =====Irrigação Inteligente=====
# Projeto desenvolvido por alunos da disciplina Sitemas Distribuídos
# ministrada pelo docente Sérgio Ribeiro.

# ====INSTALAÇÕES====
# pip install pyzmq   : ZeroMQ
# pip install fastapi : FastAPI (framework utilizado para criação de APIs)
# pip install uvicorn : servidor web para Python - utilizado pelo FastAPI.
#Para iniciar o servidor : python -m uvicorn subscriber:app --reload

# =====SUBSCRIBER=====
# Responsável pelo recebimento de dados provindos do ESP32 e também 
# pela disponibização de endpoints para que seja realizada a integração
# Telegram - Servidor.

import zmq
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/RegarOuNao")
def getRegarOuNao():
    
    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://192.168.100.5:2020")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"umidade")

    poller = zmq.Poller()
    poller.register(subscriber, zmq.POLLIN)

    try:
        socks = dict(poller.poll())
    except KeyboardInterrupt:
        exit()

    if subscriber in socks:
        [address, contents] = subscriber.recv_multipart()
        conteudo = json.loads(contents)
        regarOuNao = conteudo["regarOuNao"]
        return regarOuNao

    subscriber.close()
    context.term()
