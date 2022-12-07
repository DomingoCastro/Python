from class35coche import Coche
from class35deportivo import Deportivo

import random

# VAMOS A GENERAR NUMEROS ALEATORIOS 
# Y RECUPERAMOS UN NUMERO ENTERO ENTRE 1 Y 50
aleatorio = random.randint(1, 50)
print (aleatorio)



print("Conduciendo mi deportivo")

car = Deportivo()
car.marca = "Ferrari"
car.modelo = "F40"
opcion = -1
while (opcion != 0):
    print("---------")
    print("0.- Salir")
    print("1.- Arrancar")
    print("2.- Acelerar")
    print("3.- Frenar")
    print("4.- Detener")
    print ("5.- Turbo")
    print("Seleccione una opcion")
    opcion = int(input())
    if opcion == 1:
        car.arrancar()
    elif opcion == 2:
        car.acelerar()
    elif opcion == 3:
        car.frenar()
    elif opcion == 4:
        car.detener()
    elif opcion == 5:
        car.turbo()
    elif opcion == 0:
        print("Saliendo...")
    else:
        print("Opcion incorrecta")
print("FIN DE PROGRAMA")