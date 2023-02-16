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


import time
import zmq
import json
from fastapi import FastAPI

app = FastAPI()

base_url = "192.168.100.22"
statusPort = "2020"
paramsPort = "2021"
urlStatus = f"tcp://{base_url}:{statusPort}"
urlParams = f"tcp://{base_url}:{paramsPort}"


def receive_status():
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
        subscriber.close()
        context.term()
        return conteudo


def send_params():
    send_context = zmq.Context()
    publisher = send_context.socket(zmq.PUB)
    publisher.bind(urlParams)

    publisher.send_multipart([b"params", b'{ "cultura":"Alface"}'])
    publisher.close()
    send_context.term()


def main():
    while True:
        print(receive_status())


@app.get("/")
def getData():
    return receive_status()


# @app.post("/")
# def postData():
#     return send_params()


if __name__ == "__main__":
    main()
