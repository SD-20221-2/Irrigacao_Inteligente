import Pyro4
aposentadoria = Pyro4.Proxy("PYRONAME:aposentadoria")

idade = int(input("Qual a idade do funcionário? "))

tempoServico = int(input("Qual o tempo de serviço do funcionário? "))

print(aposentadoria.podeAposentar(idade,tempoServico))