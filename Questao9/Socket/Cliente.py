import socket

HOST = 'localhost'

PORT = 5000        

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destino = (HOST, PORT)

tcp.connect(destino)

print('\nDigite suas mensagens')

mensagem = input()

tcp.send(str(mensagem).encode())

mensagem = input()

tcp.close()
