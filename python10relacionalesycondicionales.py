from math import trunc
print ("Numero de horas")
nhoras = int(input())
print ("Precio por hora")
phora = int(input())
print ("Kilometros recorridos")
kilometros = int(input())
horasextras = 0
sueldobase = 0
sueldo = 0
sueldoextra = 0
if (kilometros < 100):
    print("DIETAS LOCALES")
elif (kilometros > 100 and kilometros < 501) :
    print ("DIETAS NACIONALES")
else:
    print ("DIETAS INTERNACIONALES")
if (nhoras > 36):
    horasextras = nhoras - 36
    sueldobase = nhoras * phora - (horasextras * phora )
    sueldo = sueldobase + horasextras * (phora + 2)
    sueldoextra = horasextras * phora
else:
    horasExtras = 0
    sueldo = nhoras * phora
    sueldobase = nhoras * phora - (horasextras * phora )
    sueldoextra = horasextras * phora
if (sueldo < 250):
    print ("NO TIENE RETENCION")
elif (sueldo >= 251 and sueldo <= 800):
    print ("RETENCION DEL 20%")
else:
    print ("RETENCION 40%")

print ("EL sueldo total es: " + str(sueldo))
print ("El salario extra es: " + str(sueldoextra))
print ("El salario base es: " + str(sueldobase))
print("FIN DEL PROGRAMA")
