import Pyro4
import random
import os

@Pyro4.expose
class Aposentadoria(object):
    def podeAposentar(self, idade, tempoServico):
        if idade >= 65 or tempoServico >= 30 or (idade >= 60 & tempoServico >= 25):
            return "Pode se aposentar!"
        else: 
            return "Não pode se aposentar!"

daemon = Pyro4.Daemon(host='localhost')    
ns = Pyro4.locateNS()
uri = daemon.register(Aposentadoria)
ns.register("aposentadoria", uri)

print("Olá, o servidor pode ser usado.")
daemon.requestLoop()  
 

