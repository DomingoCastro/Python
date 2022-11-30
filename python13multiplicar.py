print("TABLA MULTIPLICAR")
print ("ESCRIBE EL NUMERO QUE DESEAS MULTIPLICAR")
numero = int(input())
print ("¿Hasta que numero quieres multiplicar?")
multiplicador = int(input())
print ("Iniciando Multiplicación...")
for i in range(multiplicador + 1):
    multiplicacion = numero * i
    print( str(numero) + " * " + str(i) + " = "+ str(multiplicacion))

print("Multiplicación realizada con exito. Finalizando programa...")
print("-----------------------")
print ("PROGRAMA FINALIZADO")