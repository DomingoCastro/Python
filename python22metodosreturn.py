# Metodos retunr
def convertirMayusculas(texto):
    return texto.upper()

def convertirMinusculas(texto):
    return texto.lower()

def mostrarMenu():
    print("SELECCIONE UNA OPCION")
    print("1.- Convertir minusculas")
    print("2.- Convertir a mayusculas")

# PROGRAMA PRINCIPAL
print("METODOS RETURN")
print("INTRODUZCA UN TEXTO")
valor = input()
#Metodo de accion
mostrarMenu()

#Capturamos lo que el usuario a escrito o 1 o 2

opcion = int(input())
if (opcion == 1):
    valor = convertirMinusculas(valor)
    print ("Minusculas: " + valor)
else:
    valor = convertirMayusculas(valor)
    print ("Mayusculas: " + valor)

print("FIN DE PROGRAMA")


