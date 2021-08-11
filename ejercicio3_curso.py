# escribir una función que enncuentre el elemento menor de una lista
lista = [1,2,3,4,5,6,10,22,33,-44,55]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor', menor)
