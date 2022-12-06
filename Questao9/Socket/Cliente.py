import socket

HOST = 'localhost'     # Endereço IP do Servidor

PORT = 5000        

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destino = (HOST, PORT)

tcp.connect(destino)

print('\nDigite suas mensagens')

mensagem = input()

tcp.send(str(mensagem).encode())

mensagem = input()

tcp.close()

PORT = 8080

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

        print('\nCliente..:', cliente)

        print('Mensagem.:', mensagem.decode())

        print('Finalizando conexão do cliente', cliente)
        conexao.close()
