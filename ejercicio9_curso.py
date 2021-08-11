#Definir una función que reciba nombre y apellido y los vaya agregando a un archivo interectuando con el usuario, repositorio GIT
import os
os.system('cls') 

nombreOri = input('Escribe un nombre ')
apellidoOri = input('Escribe un Apellido ')
nombre = nombreOri.capitalize()
apellido = apellidoOri.capitalize()

def agregaNombreArchivo(nombre,apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregaNombreArchivo(nombre, apellido)     
print('Se agregó exitosamente el nombre y apellido al archivo ')