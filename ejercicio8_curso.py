#Recibir una cantidad infinita de números hasta que el usuario escriba salir

print('Escribe un número, para salir del programa solo escribe "salir" ')
lista=[]

while True:
    instruccion = input('Ingrese número: ')
    instruccionMin = instruccion.lower()
    if instruccionMin == 'salir':
        break
    else:
        try:
            valor =int(instruccionMin)
            lista.append(valor)
        except:
            print('Dato inválido')
            exit()    

resultado = 0
for x in lista:
    resultado += x

nResultado = str(resultado)
print('La sumatoría de todos los valores es '+nResultado)
