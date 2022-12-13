import Pyro4
carta = Pyro4.Proxy("PYRONAME:carta")

valor = input("Qual o valor da carta?")

naipe = input("Qual o naipe da carta?")

print(carta.nomeCarta(valor,naipe))