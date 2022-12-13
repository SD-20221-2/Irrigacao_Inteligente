import Pyro4
import random
import os

@Pyro4.expose
class Carta(object):
    def nomeCarta(self, valor, naipe):
        if naipe == '1':
            naipe = 'ouros'
        elif naipe == '2':
            naipe = 'paus'
        elif naipe == '3':
            naipe = 'copas'
        else: 
            naipe = 'espadas'
        return valor + " de " + naipe

daemon = Pyro4.Daemon(host='localhost')    
ns = Pyro4.locateNS()
uri = daemon.register(Carta)
ns.register("carta", uri)

print("Olá, o servidor pode ser usado.")
daemon.requestLoop()  
 

