import socket, pickle

port = 7000 
host = "localhost"

addr = ((host,port)) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr) 

N1 = input("Digite a Nota 1: ")
N2 = input("Digite a Nota 2: ")
N3 = input("Digite a Nota 3: ")

data = [N1, N2, N3]
data_string = pickle.dumps(data)
client_socket.send(data_string)

received_data = client_socket.recv(1024)
received_data = received_data.decode()

print("A sua situação no curso é: ", received_data)

client_socket.close()
