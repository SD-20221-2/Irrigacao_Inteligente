import time
import paho.mqtt.client as mqtt
from fastapi import FastAPI
import uvicorn
import threading
import random

app = FastAPI()

# broker = "l828da7e.ala.us-east-1.emqxsl.com"
# broker = "broker.emqx.io"
broker = "0.tcp.sa.ngrok.io"
mqttPort = 11272  # porta padrão MQTT
# urlStatus = f"mqtt://{broker}:{mqttPort}"
username = "irrigacao"
password = "senha123"


def run_publisher():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt.Client("1")
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, mqttPort)

    while True:
        umidade = random.randint(0, 100)
        precisaRegar = random.randint(0, 1)
        message = f'{{"precisaRegar": {precisaRegar},"umidade":{umidade}}}'
        client.publish("status", message)
        time.sleep(5)

    client.disconnect()


def run_server():
    uvicorn.run(app, host="localhost", port=8001)


@app.get("/")
def getData():
    return ("opa")


def main():
    t1 = threading.Thread(target=run_publisher)
    t2 = threading.Thread(target=run_server)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
