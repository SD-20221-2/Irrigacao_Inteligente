import Pyro4

situacao = Pyro4.Proxy("PYRONAME:situacao")

N1 = input("Digite a Nota 1: ")
N2 = input("Digite a Nota 2: ")
N3 = input("Digite a Nota 3: ")
 
print("Sua situação é ", situacao.calculaSituacao(N1, N2, N3))
