"""
La funcion lamda esta formada por la siguiente sintaxis
lambda param1,param2..paramN: expresion.

En este ejemplo tomamos una lista para recorrer y la funcion lamba la hemos
asignado a una variable llamada res con la cual suma una unidad al valor y lo
multiplica por otro parametro que le enviemos en la llamada a la funcion.
"""
numeros = [5,7,3,6,1,8,10,24]
res = lambda x,y: (x+1) * y
for numero in numeros:
    print(res(numero,2))
