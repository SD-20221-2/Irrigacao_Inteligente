import Pyro4
idade = Pyro4.Proxy("PYRONAME:idade")

nome = input("Qual o seu nome? ")
sexo = input("Qual seu sexo? (M ou F) ")
idadeUsuario = int(input("Qual sua idade? "))

print("Você é", idade.maior_idade(sexo, idadeUsuario))
