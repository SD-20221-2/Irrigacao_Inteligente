#!/usr/bin/env python3

from threading import Thread
import socket
import pickle

HOST = "localhost"
PORT = 50001


class Th(Thread):

    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        print(addr, " conectado")

        while True:
            data = conn.recv(1024)
            if not data:
                print("Conexão encerrada")
                conn.close()
                break

            data_array = pickle.loads(data)

            data = "Error"

            if data_array[0] == "Programador":
                data = str(float(data_array[1]) * 1.18)

            if data_array[0] == "Operador":
                data = str(float(data_array[1]) * 1.2)

            conn.sendall(str.encode(data))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1000)
print("Aguardando conexão")

while True:
    conn, addr = s.accept()
    a = Th(conn, addr)
    a.start()
