import xmlrpc.client

N1 = input("Digite a Nota 1: ")
N2 = input("Digite a Nota 2: ")
N3 = input("Digite a Nota 3: ")

with xmlrpc.client.ServerProxy("http://localhost:5000/") as proxy:
    print("A sua situação é", str(proxy.calculaSituacao(N1, N2, N3)))




