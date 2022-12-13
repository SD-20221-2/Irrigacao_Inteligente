from xmlrpc.server import SimpleXMLRPCServer

def podeAposentar(idade, tempoServico):
    if idade>=65 or tempoServico>=30 or (idade>=60 & tempoServico>=25):
        return "Pode se aposentar!"
    else: 
        return "Não pode se aposentar!"

server = SimpleXMLRPCServer(("localhost", 8000))
print("Escutando a porta 8000...")
server.register_function(podeAposentar, "podeAposentar")
server.serve_forever()