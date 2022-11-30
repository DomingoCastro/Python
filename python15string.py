print("METODOS DE CLASE STRING")
texto = "Primero python"
print("METODO UPPER " + texto.upper())
print("METODO REPLACE " + texto.replace("o", "@"))
print("TEXTO[0] " + texto[0])
print("LONGITUD DE TEXTO " + str(len(texto)))
print("BUSCAR TEXTO " + str(texto.find("p")))
print("BUSCAR TEXTO " + str(texto.find("p")))
print("find sobrecarga p, desde posicion 1: " + str(texto.find("p", 1)))
print("REFIND: " + str(texto.rfind("p")))
print("Startwith A: " + str(texto.startswith("A")))
print("endswith N: " + str(texto.endswith("n")))
print("isdigit() " + str(texto.isdigit()))
print("isalpha() " + str(texto.isalpha()))
print("isalnum() " + str(texto.isalnum()))
# SLICING, SUBSTRING
# Queremos mostrar desde las 2 en adelante
subcadena = texto[2:]
print("posicion 2 en adelante: " + subcadena)
# Mostrar texto de posicion x a x
subcadena = texto[2:5]
print("Posicion 2 al 5: " + subcadena)
# Vamos a recorrer todos los caracteres de la cadena uno a uno
longitud = len(texto)
for i in range (longitud):
    # caputuramos cada letra
    letra = texto[i]
    print(str(i) + " " + " " + letra)
# Si deseamos pedir un numero al usuario y saber si es un numero o no
# El truco esta en almacenar en una variable string el valor que nos a dado
print ("Introduzca un numero")
aux = input()
if (aux.isdigit()):
    print("Es un numero")
else:
    print("ILLO UN NUMERO CABESA QUE ERES BOBO")
print("-----------------------------------")
print ("FIN DEL PROGRAMA")
