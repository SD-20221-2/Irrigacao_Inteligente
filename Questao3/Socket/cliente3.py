#!/home/lays/SD python3

#Importar bilbioteca de soquetes
import socket

HOST = 'localhost'
PORT = 8500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

nome = input()
N1 = input()
N2 = input()
N3 = input()

messagem = str(nome + '/' + N1 + '/' + N2 + '/' + N3)


s.sendall(str.encode(messagem))

data = s.recv(1024)

data = data.decode()

if data == 'aprovado':
	print(nome,'foi aprovado.')
else:
	print(nome,'não foi aprovado.')
