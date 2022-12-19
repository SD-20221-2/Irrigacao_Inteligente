from threading import Thread
import socket
import pickle

class Th(Thread):

    def __init__ (self):
        Thread.__init__(self)

    def run(self):
        
        HOST = 'localhost'

        PORT = 5000        

        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        destino = (HOST, PORT)

        tcp.connect(destino)

        data = [45, 35]
        data_string = pickle.dumps(data)

        tcp.send(data_string)

        received_data = tcp.recv(1024)
        received_data = received_data.decode()
        print(received_data)


for i in range(500):
    a = Th()
    a.start()