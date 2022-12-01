print("Dame unos numeros que sumar (TODOS JUNTOS)")
aux = input()
while (aux.isdigit() == False):
    print("SOLO NUMEROS")
    aux = input()
longitud = len(aux)
suma = 0
for i in range (longitud):
    caracter = aux[i]
    numero = int(caracter)
    suma = suma + numero
    print("la suma es de " + aux + " es " + str(suma))