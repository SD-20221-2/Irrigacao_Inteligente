import Pyro4
pesoIdeal = Pyro4.Proxy("PYRONAME:pesoIdeal")

altura = input("Qual é a sua altura? ")
peso = input("Qual é o seu peso? ")
sexo = input("Qual é o seu sexo? ")
 
print("Seu peso ideal é: " , pesoIdeal.calculaPesoIdeal(altura,sexo))
