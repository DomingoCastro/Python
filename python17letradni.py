from math import trunc
print("Escribe tu DNI")
dni = (input())
if (dni.isdigit() == False):
    print("DEBE SER SOLO NUMEROS")
elif len(dni) != 8 :
    print ("DEBE TENER 8 CARACTERES")
else:
    dni = int(dni)
    operacion = (dni - (trunc(dni / 23) * 23))
    cadena = "TRWAGMYFPDXBNJZSQVHLCKET" 
    letra = cadena[operacion]
    print("Su letra del dni es " + letra)
