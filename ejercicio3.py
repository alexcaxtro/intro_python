#Ejercicio 3: Obtener la fecha y hora actuales del sistema

import datetime

ahora =datetime.datetime.now()

print(ahora)
print(type(ahora))

print(ahora.strftime('%d/%m/%Y %H:%M:%S'))
