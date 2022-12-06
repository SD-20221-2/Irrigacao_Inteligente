from xmlrpc.server import SimpleXMLRPCServer

def maior_idade(sexo, idadeUsuario):
    if sexo == "M" and idadeUsuario >= 18:
        return "maior de idade"
    elif sexo == "F" and idadeUsuario >= 21:
        return "maior de idade"
    else:
        return "menor de idade"


server = SimpleXMLRPCServer(("localhost", 5000))
print("Escutando a porta 5000")
server.register_function(maior_idade, "maior_idade")
server.serve_forever()
