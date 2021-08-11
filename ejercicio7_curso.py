#Escribir una función que indique cuántas vocales tiene
palabraOriginal = input('Escriba una palabra y te diré cuantas vocales tiene ')
palabra = palabraOriginal.lower()
vocales = 0

for x in palabra:
    vocales +=1 if x == 'a' or x =='e' or x=='i' or x=='o' or x == 'u' else 0
nVocales = str(vocales)
print('La palabra '+ palabraOriginal + ' tiene ' + nVocales +' vocales')    