import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("Resposta: %s" % str(proxy.nomeCarta(5,2)))