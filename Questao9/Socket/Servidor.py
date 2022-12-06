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

        naipe = mensagem.decode().split()[0]
        valor = mensagem.decode().split()[1]
        if naipe == '1':
            naipe = 'ouros'
        elif naipe == '2':
           naipe = 'paus'
        elif naipe == '3':
           naipe = 'copas'
        else: 
           naipe = 'espadas'
        tcp.send(str(valor + " de " + naipe).encode())
        tcp.close()