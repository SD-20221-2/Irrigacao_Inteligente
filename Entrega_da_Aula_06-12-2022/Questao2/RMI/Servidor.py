import Pyro4
import random
import os


@Pyro4.expose
class Idade(object):
    def maior_idade(self, sexo, idadeUsuario):
        if sexo == "M" and idadeUsuario >= 18:
            return "maior de idade"
        elif sexo == "F" and idadeUsuario >= 21:
            return "maior de idade"
        else:
            return "menor de idade"


daemon = Pyro4.Daemon(host='localhost')
ns = Pyro4.locateNS()
uri = daemon.register(Idade)
ns.register("idade", uri)

print("Servidor rodando no endereço:", uri)
daemon.requestLoop()
