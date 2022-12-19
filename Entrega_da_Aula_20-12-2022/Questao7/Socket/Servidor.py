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

            if data_array[0]>=65 or data_array[1]>=30 or (data_array[0]>=60 & data_array[1]>=25):
                mensagem = "Pode se aposentar!"
            else: 
                mensagem = "Não pode se aposentar!"

            conexao.sendall(str.encode(mensagem))      

HOST = 'localhost'
PORT = 5000

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
