from xmlrpc.server import SimpleXMLRPCServer

def nomeCarta(self, valor, naipe):
    if naipe == '1':
        naipe = 'ouros'
    elif naipe == '2':
        naipe = 'paus'
    elif naipe == '3':
        naipe = 'copas'
    else: 
        naipe = 'espadas'
    return valor + " de " + naipe

server = SimpleXMLRPCServer(("localhost", 8000))
print("Escutando a porta 8000...")
server.register_function(nomeCarta, "nomeCarta")
server.serve_forever()