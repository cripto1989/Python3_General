"""
List Comprehensions nos permite recorrer una lista, manipulando el elemento que
se esta iterando en el momento, agregando condicionales
"""
numeros = [5,3,1,4,9,8,7,5,2]
lista2 = [num for num in numeros]
# Asi tambien realizar operaciones con el mismo concepto
#lista2 = [(num * 3) for num in numeros]

# Agregando un condicional al momento de recorrer la lista para determinar
#elementos
#lista2 = [num for num in numeros if num % 2 ==0]
print ("Lista 2 es {}".format(lista2))
