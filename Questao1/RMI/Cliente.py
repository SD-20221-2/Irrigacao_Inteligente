import Pyro4
reajuste = Pyro4.Proxy("PYRONAME:reajuste")

nome = input("Qual o nome do funcionário? ")
cargo = input("Qual o cargo do funcionário? ")
salario = float(input("Qual o salário do funcionário? "))
 
print("Olá, o novo salário de", nome, "é:", reajuste.salarioReajustado(cargo, salario))
