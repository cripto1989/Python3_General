lista = [2,4,6,8,1,3,7,9,5,10,14,9]

nueva_lista = list(map(lambda n: n * 2, lista))

lista_pares = list(filter(lambda n: n % 2 == 0, lista))
lista_tercios = list(filter(lambda n: n % 3 == 0, lista))


from functools import reduce
product = reduce( (lambda x, y: x + y), [1, 2, 3, 4] )
print(product)
