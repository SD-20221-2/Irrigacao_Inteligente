import Pyro4
import random
import os

@Pyro4.expose
class salarioLiq(object):
	def calculoLiquido(self,nome,nivel,sal_bruto,n_dependentes):
		if nivel == 'A':
			if n_dependentes > 0:
				sal_bruto *= 0.08
			else:
				sal_bruto *= 0.03
		elif nivel == 'B':
			if n_dependentes > 0:
				sal_bruto *= 0.1
			else:
				sal_bruto *= 0.05
		elif nivel == 'C':
			if n_dependentes > 0:
				sal_bruto *= 0.15
			else:
				sal_bruto *= 0.08	
		elif nivel == 'D':
			if n_dependentes > 0:
				sal_bruto *= 0.17
			else:
				sal_bruto *= 0.1
			
daemon = Pyro4.Daemon(host = 'localhost')
ns = Pyro4.locateNS()
uri = daemon.register(salarioLiq)
ns.register("salarioLiq",uri)

print("Sevidor rodando no endereço:", uri)
daemon.requestLoop()
