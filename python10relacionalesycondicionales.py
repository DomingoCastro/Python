from math import trunc
print ("Numero de horas")
nhoras = int(input())
print ("Precio por hora")
phora = int(input())
print ("Kilometros recorridos")
kilometros = int(input())
horasextras = nhoras - 36
sueldobase = nhoras * phora - (horasextras * phora )
sueldo = sueldobase + horasextras * (phora + 2)
if (kilometros < 100):
    print("DIETAS LOCALES")
elif (kilometros > 100 and kilometros < 501) :
    print ("DIETAS NACIONALES")
else:
    print ("DIETAS INTERNACIONALES")

if (sueldo < 250):
    print ("NO TIENE RETENCION")
elif (sueldo >= 251 and sueldo <= 800):
    print ("RETENCION DEL 20%")
else:
    print ("RETENCION 40%")

print ("EL sueldo total es: " + str(sueldo))
print("FIN DEL PROGRAMA")
