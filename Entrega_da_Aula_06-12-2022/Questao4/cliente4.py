#!/home/lays/SD python3

#Importar bilbioteca de soquetes
import socket

HOST = 'localhost'
PORT = 8500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

altura = input()
peso = input()
sexo = input()

messagem = str(altura + '/' + peso + '/' + sexo)


s.sendall(str.encode(messagem))

data = s.recv(1024)

data = data.decode()

print('Peso atual:', peso)
print('Peso ideal:', data)
