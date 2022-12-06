import socket

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

        print('\nCliente..:', cliente)

        print('Mensagem.:', mensagem.decode())

        print('Finalizando conexão do cliente', cliente)
        conexao.close()

        PORT = 8080

        destino = (HOST, PORT)

        tcp.connect(destino)

        if int(mensagem.decode().split()[0])>=65 or int(mensagem.decode().split()[1])>=30 or int((mensagem.decode().split()[0])>=60 & int(mensagem.split()[1])>=25):
                tcp.send(str("Pode se aposentar!").encode())
        else: 
            tcp.send(str("Não pode se aposentar!").encode())

        tcp.close()