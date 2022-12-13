from xmlrpc.server import SimpleXMLRPCServer

def salarioReajustado(cargo, salario):
    if cargo == "Operador":
        return salario * 1.2
    elif cargo == "Programador":
        return salario * 1.18
    else:
        return "error"


server = SimpleXMLRPCServer(("localhost", 5000))
print("Escutando a porta 5000")
server.register_function(salarioReajustado, "salarioReajustado")
server.serve_forever()
