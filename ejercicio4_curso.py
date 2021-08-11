#escribir una función que devuelva el volumen de una esfera por su radio

radio= input('Escribe un número para el radio de la esfera y devuelvo su volumen ')
r = int(radio)

def calcularVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calcularVolumen(r)

print(resultado)