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
	
	nome,N1,N2,N3 = data.split('/')
	
	N1 = float(N1)
	N2 = float(N2)
	N3 = float(N3)
	
	M = (N1+N2)/2
	
	if M >= 7:
		data = 'aprovado'
	elif M > 3 and M < 7:
		if (M + N3)/2 >= 5:
			data = 'aprovado'
		else:
			data = 'reprovado'
	else:
		data = 'reprovado'
		
	data = str.encode(data)
	conn.sendall(data)
