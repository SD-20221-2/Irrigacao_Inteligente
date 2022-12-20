import socket
import _thread

HOST = 'localhost'
PORT = 8050

def conectado(con,cliente):

	print('\nCLiente conectado:',cliente)

	while True:
		data = con.recv(1024)
		if not data:
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

		print('\nCliente:', cliente)
		print('Mensagem:',data)

	print('\nFinalizando conexao do cliente',cliente)

	con.close()
	_thread.exit()

tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
orig = (HOST,PORT)

tcp.bind(orig)

tcp.listen(1)

print('\nServidor TCP concorrente iniciado no IP',HOST,'na porta',PORT)

while True:

	con,cliente = tcp.accept()

	print('\nNova thread iniciada para essa conexão')

	_thread.start_new_thread(conectado,tuple([con,cliente]))

tcp.close()