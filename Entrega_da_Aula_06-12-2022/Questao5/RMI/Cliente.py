import Pyro4
categoria = Pyro4.Proxy("PYRONAME:categoria")

idade = input("Qual a idade?")

print("Categoria: ",categoria.calculoCategoria(idade))
