"""
Escribe una función llamada "duplicado" que tome una lista y devuelva True si tiene algún elemento duplicado. La función
no debe modificar la lista.

Crear una función que genere una lista de 23 números aleatorios del 1 al 100 y comprobar con la función anterior si
existen elementos duplicados. (Puedes ver el módulo random como guía)
"""

import random

lista = []


def genera_lista():
    while len(lista) < 23:
        lista.append(random.randrange(100))


def duplicados():
    if len(frozenset(lista)) < len(lista):
        return True
    else:
        return False


genera_lista()
print(lista)
print(set(lista))
print(duplicados())
