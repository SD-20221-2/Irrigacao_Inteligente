from threading import Thread
import socket
import pickle

class Th(Thread):

    def __init__ (self, conexao, cliente):
        Thread.__init__(self)
        self.conexao = conexao
        self.cliente = cliente

    def run(self):

        print('\nConexão realizada por:', self.cliente)

        while True:

            mensagem = self.conexao.recv(1024)

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

HOST = 'localhost'
PORT = 8080

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)
tcp.bind(origem)

#Tolera até 500 conexões
tcp.listen(500)

print('\nServidor TCP iniciado no IP', HOST, 'na porta', PORT)

while True:
    conexao, cliente = tcp.accept()
    a = Th(conexao, cliente)
    a.start()