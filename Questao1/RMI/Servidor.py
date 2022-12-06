import Pyro4
import random
import os


@Pyro4.expose
class Reajuste(object):
    def salarioReajustado(self, cargo, salario):
        if cargo == "Operador":
            return salario * 1.2
        elif cargo == "Programador":
            return salario * 1.18
        else:
            return "error"


daemon = Pyro4.Daemon(host='localhost')
ns = Pyro4.locateNS()
uri = daemon.register(Reajuste)
ns.register("reajuste", uri)

print("Servidor rodando no endereço:", uri)
daemon.requestLoop()
