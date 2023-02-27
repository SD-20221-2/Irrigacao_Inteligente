import time
import json
import paho.mqtt.client as mqtt
from fastapi import FastAPI
import uvicorn
import threading
import random

app = FastAPI()

base_url = "localhost"
statusPort = 1883  # porta padrão MQTT
urlStatus = f"mqtt://{base_url}:{statusPort}"


def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao broker com resultado {rc}")


def run_publisher():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(base_url, statusPort)

    while True:
        umidade = random.randint(0, 9999)
        message = f'{{"precisaRegar":true,"umidade":{umidade}}}'
        client.publish("status", message)
        time.sleep(1)

    client.disconnect()


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
