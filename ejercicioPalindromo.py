import os
os.system('cls') 
inverso = ""

palabra = input("Escriba una palabra y te diré si es un palíndromo: ")
print (palabra)
inverso = palabra[::-1]

if palabra == inverso:
    print('Es una palabra palindromo')
else:
    print('No es palindromo')
