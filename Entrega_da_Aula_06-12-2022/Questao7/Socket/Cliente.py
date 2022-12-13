import socket
import pickle

HOST = 'localhost'

PORT = 5000        

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destino = (HOST, PORT)

tcp.connect(destino)

idade = input("Digite a idade do funcionário:")
tempoServico = input("Digite o tempo de serviço:")

data = [idade, tempoServico]
data_string = pickle.dumps(data)

tcp.send(data_string)

received_data = tcp.recv(1024)
received_data = received_data.decode()

print(received_data)