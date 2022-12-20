from xmlrpc.server import SimpleXMLRPCServer

def categoria(data):
	
	if data >= 5 and data <= 7:
		data = 'infatil A'
	elif data >= 8 and data <= 10:
		data = 'infantil B'
	elif data >= 11 and data <= 13:
		data = 'juvenil A'
	elif data >= 14 and data <= 17:
		data = 'juvenil B'
	elif data >= 18:
		data = 'adulto'
		
	return data
	
	
server = SimpleXMLRPCServer(("localhost",8050))
print("Conexão estabelecida na porta 8050")
server.register_function(categoria, "categoria")
server.serve_forever()
