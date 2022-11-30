print ("NUMEROS PARES")
print("Escribe uno numero")
inicio = int(input())
print ("numero final")
fin = int(input())
for i in range (inicio, fin + 1):
    if (i % 2 == 0):
        print ("PAR " + str(i))
print  ("FIN PROGRAMA")