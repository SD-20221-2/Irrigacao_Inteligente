
import paho.mqtt.client as mqtt
from struct import pack
from random import randint
from time import sleep

AREA_ID = 10
SENSOR_ID = 5000

# topicos providos por este sensor
ut = "area/%d/sensor/%s/umidade" % (AREA_ID, SENSOR_ID)

# cria um identificador baseado no id do sensor
client = mqtt.Client(client_id='NODE:%d-%d' % (AREA_ID, SENSOR_ID),
                     protocol=mqtt.MQTTv31)
# conecta no broker
client.connect("127.0.0.1", 1883)

while True:
    # gera um valor de umidade aleatório
    u = randint(0, 100)
    # codificando o payload como big endian, 2 bytes
    payload = pack(">H", u)
    # envia a publicação
    client.publish(ut, payload, qos=0)
    print(ut + "/" + str(u))

    sleep(5)
