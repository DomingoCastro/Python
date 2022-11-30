numero = 0
pregunta = "S"
while pregunta == "S" :
    print("Escribe un numero")
    numero = int(input())
    if numero > 0:
        print("POSITIVO " + str(numero))
    elif numero == 0: 
        print("NUMERO NEUTRAL 0")
    else:
        print("NEGATIVO " + str(numero))
    print("¿DESEA CONTINUAR? (N PARA NO, S PARA SI)")
    pregunta = (input())

print("FIN DE PROGRAMA")
            