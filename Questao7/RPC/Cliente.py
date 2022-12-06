import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("Resposta: %s" % str(proxy.podeAposentar(56,15)))