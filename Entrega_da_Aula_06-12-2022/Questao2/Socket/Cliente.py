#!/usr/bin/env python3

import socket
import pickle

HOST = "localhost"
PORT = 50001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M ou F): ")
idade = input("Digite sua idade: ")

data = [sexo, idade]
data_string = pickle.dumps(data)

server.send(data_string)

received_data = server.recv(1024)
received_data = received_data.decode()

print("Olá", nome, "voce é", received_data)
