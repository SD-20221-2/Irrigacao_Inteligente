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
	
	altura,peso,sexo = data.split('/')
	
	altura = float(altura)
	peso = float(peso)
	
	if sexo == 'masculino':
		data = (altura*72.7) - 58
	elif sexo == 'feminino':
		data = (altura*62.1) - 44.7

	
	data = str.encode(str(data))
	conn.sendall(data)
