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

        if data_array[0]>=65 or data_array[1]>=30 or (data_array[0]>=60 & data_array[1]>=25):
            mensagem = "Pode se aposentar!"
        else: 
            mensagem = "Não pode se aposentar!"

        conexao.sendall(str.encode(mensagem))      