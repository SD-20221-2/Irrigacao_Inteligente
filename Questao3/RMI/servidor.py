import Pyro4
import random
import os


@Pyro4.expose
class Situacao(object):
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


daemon = Pyro4.Daemon(host='localhost')
ns = Pyro4.locateNS()
uri = daemon.register(Situacao)
ns.register("situacao", uri)

print("Endereço do servidor:", uri)
daemon.requestLoop()
