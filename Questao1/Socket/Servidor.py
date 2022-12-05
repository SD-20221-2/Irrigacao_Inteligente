#!/usr/bin/env python3

import socket
import pickle

HOST = "localhost"
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Aguardando conexão")
conn, addr = s.accept()

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
