from xmlrpc.server import SimpleXMLRPCServer
    
def calculaSituacao(n1, n2, n3):
    media_M = (n1 + n2) / 2
    media = (media_M + n3)/2

    if media_M >= 7:
        return "Aprovado"

    elif media_M>=3 and media_M < 7:
        if media >= 5:
            return "Aprovado"
    
    else:
        return "Reprovado"


server = SimpleXMLRPCServer(("localhost", 5000))
server.register_function(calculaSituacao, "calculaSituacao")
server.serve_forever()
