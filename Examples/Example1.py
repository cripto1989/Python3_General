"""
Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, una nueva lista donde el
primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo, el tercer elemento es la suma
del resultado anterior con el siguiente elemento y así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es
[1, 3, 6].
"""
class Operacion():
    lista = [5, 3, 9, 7, 6, 1, 2, 8, 4, 5]
    new_list = [lista[0]]

    @classmethod
    def sumar_listas(self):
        for li in self.lista[1:len(self.lista)]:
            self.new_list.append(self.new_list[len(self.new_list) - 1] + li)
        return self.new_list
print(Operacion.sumar_listas())
