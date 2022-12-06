import Pyro4
import random
import os

@Pyro4.expose
class Categoria(object):
	def calculoCategoria(self,idade):
		if idade >= 5 and idade <= 7:
			idade = 'infatil A'
		elif idade >= 8 and idade <= 10:
			idade = 'infantil B'
		elif idade >= 11 and idade <= 13:
			idade = 'juvenil A'
		elif idade >= 14 and idade <= 17:
			idade = 'juvenil B'
		elif idade >= 18:
			idade = 'adulto'
			
daemon = Pyro4.Daemon(host = 'localhost')
ns = Pyro4.locateNS()
uri = daemon.register(Categoria)
ns.register("Categoria",uri)

print("Sevidor rodando no endereço:", uri)
daemon.requestLoop()
