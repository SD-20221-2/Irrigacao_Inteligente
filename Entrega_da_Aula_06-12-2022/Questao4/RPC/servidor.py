from xmlrpc.server import SimpleXMLRPCServer

def calculaPesoIdeal(altura, peso, sexo):

	if sexo == 'masculino':
		return (altura*72.7) - 58
	elif sexo == 'feminino':
		return (altura*62.1) - 44.7


server = SimpleXMLRPCServer(("localhost", 5000))
server.register_function(calculaPesoIdeal, "calculaPesoIdeal")
server.serve_forever()
