import Pyro4
import random
import os


@Pyro4.expose
class PesoIdeal(object):
    def calculaPesoIdeal(self, altura, sexo):
        if sexo == 'masculino':
            return (altura*72.7) - 58
	    
        elif sexo == 'feminino':
	        return (altura*62.1) - 44.7


daemon = Pyro4.Daemon(host='localhost')
ns = Pyro4.locateNS()
uri = daemon.register(PesoIdeal)
ns.register("pesoIdeal", uri)

print("Endereço do servidor:", uri)
daemon.requestLoop()
