import time
import zmq
from fastapi import FastAPI
import uvicorn
import threading
import random

app = FastAPI()

base_url = "192.168.100.22"
statusPort = "2020"
paramsPort = "2021"
urlStatus = f"tcp://{base_url}:{statusPort}"
urlParams = f"tcp://{base_url}:{paramsPort}"


def run_publisher():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind(urlStatus)

    while True:
        umidade = random.randint(0, 9999)
        message = f'{{"precisaRegar":true,"umidade":{umidade}}}'
        publisher.send_multipart(
            [b"status", message.encode('utf-8')])
        time.sleep(1)

    publisher.close()
    context.term()


def run_server():
    uvicorn.run(app, host="localhost", port=8001)


@app.get("/")
def getData():
    return ("opa")


def main():
    t1 = threading.Thread(target=run_server)
    t2 = threading.Thread(target=run_publisher)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

# ------------------------------------------------------------------------

# import json
# import time
# import zmq

# base_url = "192.168.100.22"
# statusPort = "2020"
# paramsPort = "2021"
# urlStatus = f"tcp://{base_url}:{statusPort}"
# urlParams = f"tcp://{base_url}:{paramsPort}"


# def receive_data():
#     get_context = zmq.Context()
#     subscriber = get_context.socket(zmq.SUB)
#     subscriber.connect(urlParams)
#     subscriber.setsockopt(zmq.SUBSCRIBE, b"umidade")

#     poller = zmq.Poller()
#     poller.register(subscriber, zmq.POLLIN)

#     try:
#         socks = dict(poller.poll(1000))
#     except KeyboardInterrupt:
#         subscriber.close()
#         get_context.term()
#         exit()

#     if subscriber in socks:
#         [address, contents] = subscriber.recv_multipart()
#         conteudo = json.loads(contents)
#         subscriber.close()
#         get_context.term()
#         print(conteudo)
#         return conteudo


# def send_data(data):
#     send_context = zmq.Context()
#     publisher = send_context.socket(zmq.PUB)
#     publisher.bind(urlStatus)

#     publisher.send_multipart([b"status", json.dumps(data).encode()])
#     publisher.close()
#     send_context.term()


# def main():
#     while True:
#         data = receive_data()
#         if data:
#             # Aqui você pode fazer o processamento necessário com os dados recebidos
#             print("Dados recebidos:", data)

#         send_data({"precisaRegar": False, "umidade": 30})
#         time.sleep(1)


# if __name__ == "__main__":
#     main()
