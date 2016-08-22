"""
La compresion de listas permite manipular las listas mediante un for dentro de la misma
"""
lista = [x for x in range(5,20)]

# Realizando operaciones dentro de ella
lista2 = [x * 0.5 for x in lista]

# Condicionando ciertos elementos
lista3 = [x for x in lista if x % 2 == 0]

# Restringiendo algunos elementos
no_primos = [j for i in range(2,8) for j in range(i*2,50,i)]
primos = [ n for n in range(1,50) if n not in no_primos]

# Creando otros elementos
frase = "hola mundo como estas".split()
conjunto = [[pal.upper(), pal.lower(), len(pal)] for pal in frase]
