from python26funcionestools import *
import datetime
print("Elige que deseas hacer")
menuBisiestoyNarcicista()
opcion = int(input())
if (opcion == 1):
    print("Introduzca un año")
    anyo = int(input())
    respuesta = isBisiesto(anyo)
    if (respuesta == True):
        print("El año es bisiesto")
    else:
        print("Año NO bisiesto")
elif (opcion == 2):
    print("Introduce un número")
    textoNumero = input()
    respuesta = isNarcisista(textoNumero)
    if (respuesta == True):
        print("Es un número narcisista")
    else:
        print("Lo siento, su número NO es narcisista")
elif opcion == 3:
    print("Introduce el año de nacimiento")
    anyoNacimiento= int(input())
    fechaActual= datetime.date.today()
    anyoActual= int(fechaActual.year)
    for i in range(anyoNacimiento, anyoActual + 1):
        if (isBisiesto(int(i))):
            print(i)
elif opcion == 0:
    print("Graicas por usar el programa")
else:
    print("Esa opcion no es valida")