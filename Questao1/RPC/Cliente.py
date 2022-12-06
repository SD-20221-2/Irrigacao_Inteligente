import xmlrpc.client

nome = input("Qual o nome do funcionário? ")
cargo = input("Qual o cargo do funcionário? ")
salario = float(input("Qual o salário do funcionário? "))

with xmlrpc.client.ServerProxy("http://localhost:5000/") as proxy:
    print("O novo salário de", nome, "é:", "%s" %
          str(proxy.salarioReajustado(cargo, salario)))
