import sys
from threading import Thread
import socket

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
        
            mensagem = mensagem.decode("utf-8")
            data_array = mensagem.split()

            mensagem = "Error"

            idade = int(data_array[0])
            tempoServico = int(data_array[1])

            if idade>=65 or tempoServico>=30 or (idade>=60 & tempoServico>=25):
                mensagem = "Pode se aposentar!"
            else: 
                mensagem = "Não pode se aposentar!"

            conexao.sendall(str.encode(mensagem))      

HOST = 'localhost'
PORT = 1531

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