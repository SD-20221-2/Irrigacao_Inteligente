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
	nome,nivel,sal_bruto,n_dependentes = data.split('/')
	
	sal_bruto = float(sal_bruto)
	n_dependentes = int(n_dependentes)
	
	if nivel == 'A':
		if n_dependentes > 0:
			sal_bruto *= 0.08
		else:
			sal_bruto *= 0.03
	elif nivel == 'B':
		if n_dependentes > 0:
			sal_bruto *= 0.1
		else:
			sal_bruto *= 0.05
	elif nivel == 'C':
		if n_dependentes > 0:
			sal_bruto *= 0.15
		else:
			sal_bruto *= 0.08	
	elif nivel == 'D':
		if n_dependentes > 0:
			sal_bruto *= 0.17
		else:
			sal_bruto *= 0.1
	
	data = str.encode(str(sal_bruto))
	
	conn.sendall(data)
