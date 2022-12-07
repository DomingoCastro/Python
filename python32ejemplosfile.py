
try:
    print("Ejemplo ficheros Python")
    # Creamos un nuevo archivo y escribimos algo en él.
    # Voy a utilizar w+ Lectura/Escritura
    fichero = open("nombre.txt" , "w+")
    print ("Introduzca su nombre")
    nombre = input()
    #Escribimos en el archivo
    fichero.write("Su nombre es " + nombre)
    # Es recomendable/obligatorio utilizar FLUSH
    fichero.flush()
    # SIEMPRE CERRAMOS EL FICHERO PARA TODAS LAS ACCIONES.
    fichero.close()
    # A continuacion añadimos informacion al archivo creado.
    # Abrimos el archivo en modo append (a)
    archivo = open("nombre.txt", "a")
    print("Introduzca otro nombre")
    nombre = input()
    archivo.write("\nNuevo nombre: " + nombre)
    archivo.flush()
    archivo.close()
    print("Fin del programa")
    # Por ultimo, leeemos el contenido del archivo
    file = open("nombre.txt" , "r")
    contenido = file.read()
    print("-------------")
    print(contenido)
    file.close()
except : 
    print ("ERROR")
finally:
    fichero.close()
    archivo.close()
    file.close()