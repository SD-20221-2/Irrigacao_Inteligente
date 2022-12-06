import xmlrpc.client

nome = input("Qual o seu nome? ")
sexo = input("Qual seu sexo? (M ou F) ")
idadeUsuario = int(input("Qual sua idade? "))

with xmlrpc.client.ServerProxy("http://localhost:5000/") as proxy:
    print("Você é", "%s" % str(proxy.maior_idade(sexo, idadeUsuario)))
