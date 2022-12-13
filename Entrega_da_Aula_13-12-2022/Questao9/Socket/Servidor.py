import socket
import pickle

HOST = 'localhost'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)
tcp.bind(origem)
tcp.listen(1)

print('\nServidor TCP iniciado no IP', HOST, 'na porta', PORT)

while True:

   conexao, cliente = tcp.accept()

   print('\nConexão realizada por:', cliente)

   while True:

        mensagem = conexao.recv(1024)

        if not mensagem:

           break

        data_array = pickle.loads(mensagem)

        mensagem = "Error"

        valor = data_array[0]
        naipe = data_array[1]
        if naipe == '1':
            naipe = 'ouros'
        elif naipe == '2':
           naipe = 'paus'
        elif naipe == '3':
           naipe = 'copas'
        else: 
           naipe = 'espadas'
        mensagem = valor + " de " + naipe

        conexao.sendall(str.encode(mensagem))      
