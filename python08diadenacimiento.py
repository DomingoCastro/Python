from math import trunc
print("Escribe el día")
dia = int(input())
print("Escribe el mes")
mes = int(input())
print("Escribe el año")
anyo = int(input())
if (mes == 1):
    mes = 13
    anyo = anyo - 1
elif (mes == 2):
    mes = 14
    anyo = anyo - 1
op1 = trunc((mes + 1) * 3 / 5)
op2 = trunc(anyo / 4)
op3 = trunc(anyo / 100)
op4 = trunc(anyo / 400)
op5 = dia + (mes * 2) + anyo + op1 + op2 - op3 + op4 + 2
op6 = trunc(op5 / 7)
opf = op5 - (op6 * 7)
if (opf == 0):
    print("Naciste un: Sábado")
elif (opf == 1):
    print("Naciste un: Domingo")
elif (opf == 2):
    print ("Naciste un: Lunes")
elif (opf == 3):
    print("Naciste un: Martes")
elif (opf == 4):
    print("Naciste un: Miércoles")
elif (opf == 5):
    print("Naciste un: Jueves")
else:
    print("Naciste un: Viernes")

print ("FIN DE PROGRAMA")