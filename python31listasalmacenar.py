from python31listastools import *
pregunta = "s"
almacen = []
lista = []
while pregunta == "s":
    print("Escribe un nombre o escriba ok para continuar")
    nombres= input()
    opcion = 100
    if nombres != "ok":
        lista.append(nombres)
        print("Has almacenado un total de : " + str(len(lista)) + " datos")
    elif nombres == "ok":
        mostrarNombres(lista)
        menuLista()
        opcion = int(input())
    if opcion == 1:
        print("Así que un nuevo nombre...")
        mostrarNombres(lista)
    elif opcion == 2:
        print ("Ingresa el indice que borrar")
        indice = int(input())
        lista.pop(indice)
        print (" Borrando nombre a la lista")
        mostrarNombres(lista)
    elif opcion == 3:
        print("Comenzando de nuevo...")
        lista.clear()
    elif opcion == 0:
        print("Saliendo...")
        pregunta = "n"
try:
    opcion = "s"
    print("----------")
    menuLista()

except IndexError:
    print("Ha introducido un indice erroneo")
except ValueError:
    print("Debe introducir una opcion valida")
finally:
    print ("FIN DE PROGRAMA")
