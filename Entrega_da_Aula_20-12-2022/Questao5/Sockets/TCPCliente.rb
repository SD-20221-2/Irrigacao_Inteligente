require 'socket'
 
server = TCPSocket.open('localhost', 8050) # conecta ao servidor na porta 3001

print "Digite a idade:"
mensagem = gets
#messagem = str(mensagem)

while mensagem != '\x18'

	server.puts mensagem # envia mensagem para o servidor

	mensagem = gets
end

resp = server.recvfrom( 1024 ) # recebe a mensagem -1024 bytes - do servidor
puts resp
 
server.close # Fecha a conexão com o servidor
