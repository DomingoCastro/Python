def menuLista():
    print("SELECCIONE UNA OPCION")
    print("0.- Salir")
    print("1.- Añadir nombres")
    print("2.- Eliminar nombres")
    print("3.- Comenzar de nuevo")

def mostrarNombres(lista):
    # Aqui vamos a dibujar los nombres con un bucle de referencia
    # for name in nombres:
    #     print(name)
    #Lo hacemos con un bucle contador porque quiero visualizar las posicioens de cada nombre
    print("Estos son los nombres actuales: ")
    for i in range(len(lista)):
        name = lista[i]
        print(str(i) + ".- " + name)