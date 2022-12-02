def mostrarDoble():
    try:
        print("Introduzca un numero")
        numero = int(input())
        doble = numero * 2
        print("El doble del numero es " + str(doble))
    except ValueError:
        print("Error, debe introducir un número")
        print("Vuelve a introducir el numero")
        mostrarDoble()

def dividirNumero():
    try:
        print("Escribe un numero")
        numero = int(input())
        print("Escribe otro numero")
        numero2 = int(input())
        division = numero / numero2
        print("Division" + str(division))
    except ValueError:
        print("Error, solamente numeros")
    except ZeroDivisionError:
        print("No se puede dividir entre 0") 
    except:
        print("Error general")      
    finally:
        print("Siempre un finally se ejecuta y se pone al final del codigo")

print("Programa principal de control de expeciones")
dividirNumero()
try: 
    print("Conectando a la BBDD")
    print("Accediendo a los datos")
except:
    print("Error al acceder a los datos")
finally:
    print("Cerrando la base de datos")
print("Fin de programa")