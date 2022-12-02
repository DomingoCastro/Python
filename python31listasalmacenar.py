from python31listastools import *
pregunta = "s"
almacen = []
lista = []
opcion = 100
while pregunta == "s":
    print("Escribe un nombre o escriba ok para continuar")
    nombres= input()
    if nombres != "ok":
        lista.append(nombres)
        print("Has almacenado un total de : " + str(len(lista)) + " datos")
    elif nombres == "ok":
        print("Que deseas hacer con estos nombres?")
        print("Los nombres almacenados actualmente son: ")
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
print ("FIN DE PROGRAMA")
    # if nombres == nombres["ok"]:
    #     menuLista()
    #     opcion = input()
    # elif nombres != "ok" and opcion == 1:
    #     nombres.append(nombres)
    # elif nombres != "ok" and opcion == 2:
    #     print("Que indice quieres borrar")   
    #     for i in range(len(nombres)):
    #         name = nombres[i]
    #         print(str(i) + ".- " + name)
    #         indice = int(input())
    #         nombres.pop(indice)

