#!/home/lays/SD python3

#Importar bilbioteca de soquetes
import socket

HOST = 'localhost'
PORT = 8500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

nome = input()
nivel = input()
sal_bruto = input()
n_dependentes = input()


messagem = str(nome + '/' + nivel + '/' + sal_bruto + '/' + n_dependentes)

s.sendall(str.encode(messagem))

data = s.recv(1024)

data = data.decode()

print('Nome:', nome)
print('Nível:' , nivel)
print('Salário líquido:', float(sal_bruto) - float(data))
