print("Danos tu ISBN (10 CARACTERES)")
aux = input()
suma = 0
longitud = len(aux)
while (aux.isdigit() == False):
    print("Danos tu ISBN CORRECTO  (SOLO NUMEROS)")
    aux = input()
if longitud < 10 or longitud != 10 :
        print("DEBE TENER 10 CARACTERES")
else:
    for i in range(longitud):
        letra = aux[i]
        numero = int(letra)
        posicion = i + 1
        operacion = numero * posicion
        suma = suma + operacion
    if (suma % 11 == 0):
        print("Numero correcto")
    else:
        print ("Numero ISBN incorrecto")
print ("FIN DE PROGRAMA")
