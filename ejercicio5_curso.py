#Determinar si el usuario es mayor de edad

edad = input('Por favor indique su edad y yo le diré si es mayor de edad ')
n_edad = int(edad)

if n_edad > 17:
    print('Usted es mayor de edad porque usted tiene '+ edad + ' años')
else:
    print('Usted no es mayor de edad, Usted Tiene '+ edad +  ' años')    