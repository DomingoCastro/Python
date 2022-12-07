# # Tenemos una lista de ciudades
# ciudades = ["Cadiz", "Malaga", "Córdoba", "Gijon"]
# # Necesitamos almacenar la lista en un formato string
# # Para un fiche Vamos a separar los elementos con JOIN indicando un caracter (@)
# # "caracter separador".join(lista)
# contenido = "@".join(ciudades)
# print(contenido)
# # Para recuperar de un string de una lista se utiliza el metodo split
# # nombreLista = string.split(sep= "CARACTER SEPARADOR")
# cities = contenido.split("@")
# for ciudad in cities:
#     print(ciudad)
# print("FIN DE PROGRAMA")


# Declaramos coleccion para almacenar ciudades
ciudades = []
# VARIABLE GLOBAL
nombre = "Paco"

def showCiudades ():
    print("numero de ciudades: " + str(len(ciudades)))
    for ciudad in ciudades:
        print(ciudad)

# METODO PARA LEER LAS CIUDADES DE UN ARCHIVO
def leerCiudades ():
    fichero = open("ciudades.txt", "r")
    contenido = fichero.read()
    fichero.close()
    global ciudades
    # ALMACENAMOS EN CIUDADES LA INFORMACIÓN RECUPERADA
    ciudades = contenido.split(sep= "@")
    print("numero de ciudades: " + str(len(ciudades)))
    print("Datos cargados correctamente")

# METODO PARA GUARDAR LAS CIUDADES EN UN FICHERO

def saveFile():
    # CONVERTIMOS LA LISTA A STRING CON UN SEPARADOR EN ESTE CASO @
    resultado = "@".join(ciudades)
    fichero = open("ciudades.txt", "w+")
    fichero.write(resultado)
    fichero.flush()
    fichero.close()
    print("Datos almacenados correctamente")

# METODOS PARA ÑADIR CIUDADES A LA COLECCION
def insertarCiudad():
    print("Introduzca nombre de ciudad")
    ciudad = input()
    ciudades.append(ciudad)

print ("Ejemplo ciudades y files")
opcion = -1
while (opcion != 0):
    print("0.- Salir")
    print("1.- Leer ciudades")
    print("2.- Guardar file de ciudades")
    print("3.- Nueva ciudad")
    print("4.- Mostrar ciudades")
    print("Seleccione una opcion")
    opcion = int(input())
    if opcion == 1:
        print("Leyendo ciudades...")
        leerCiudades()
    elif opcion == 2:
        print("Guardando el fichero...")
        saveFile()
    elif opcion == 3:
        print("Inserta nueva ciudad")
        insertarCiudad()
    elif opcion == 4:
        print("Mostrando ciudades")
        showCiudades()
    elif opcion == 0:
        print("Saliendo del programa")
    else:
        print("Opcion incorrecta")

print("FIN DE PROGRAMA")    





