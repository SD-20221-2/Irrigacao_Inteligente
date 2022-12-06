import Pyro4
salarioLiq = Pyro4.Proxy("PYRONAME:salarioLiq")

nome = input("Qual o nome?")
nivel = input("Qual o nivel?")
sal_bruto = input("Qual o salario bruto?")
n_dependentes  = input("Qual o numero de dependentes?")

print("Nome: ",nome, " - nivel: ", nivel, " - salario liquido = ", salarioLiq.calculoLiquido(nome,nivel,sal_bruto,n_dependentes))
