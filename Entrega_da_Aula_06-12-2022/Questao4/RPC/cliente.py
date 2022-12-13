import xmlrpc.client

altura = input("Qual é a sua altura? ")
peso = input("Qual é o seu peso? ")
sexo = input("Qual é o seu sexo? ")

with xmlrpc.client.ServerProxy("http://localhost:5000/") as proxy:
    print("Seu peso ideal é", proxy.calculaPesoIdeal(altura, peso, sexo))
