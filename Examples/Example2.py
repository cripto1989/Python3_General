"""
Escribe una función llamada "elimina" que tome una lista y elimine el primer y último elemento de la lista y cree una nueva lista con los elementos que no fueron eliminados.
Luego escribe una función que se llame "media" que tome una lista y devuelva una nueva lista que contenga todos los elementos de la lista anterior menos el primero y el último.
"""
lista = [6, 4, 3, 8, 5, 2, 1, 6]
lista_dos = []


class EjemploDos():
    @classmethod
    def elimina(cls):
        lista_dos = [l for l in lista[1:(len(lista) - 1)]]
        return lista_dos


print(EjemploDos.elimina())
