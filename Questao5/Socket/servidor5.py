#!/home/lays/SD python3

#Importar bilbioteca de soquetes
import socket

HOST = 'localhost'
PORT =  8500

#AF_INET = 
#SOCK_STREAM = 


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()

print('Aguardando conexão de um cliente')
conn, ender = s.accept()

print('Conectado em', ender)

while True:
	data = conn.recv(1024)	
	
	
	if not data:
		print('Fechando conexão')
		conn.close()
		break	
	
	data = data.decode()
	
	data = int(data)
	
	if data >= 5 and data <= 7:
		data = 'infatil A'
	elif data >= 8 and data <= 10:
		data = 'infantil B'
	elif data >= 11 and data <= 13:
		data = 'juvenil A'
	elif data >= 14 and data <= 17:
		data = 'juvenil B'
	elif data >= 18:
		data = 'adulto'

	
	data = str.encode(str(data))
	conn.sendall(data)
