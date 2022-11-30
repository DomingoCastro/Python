from math import trunc
print("Escribe tu DNI")
dni = (input())
print (len(dni))
print(dni.isdigit())
dni = int(dni)
operacion = (dni - (trunc(dni / 23) * 23))
print (str(operacion))
cadena = "TRWAGMYFPDXBNJZSQVHLCKET" 
letra = cadena[operacion]
print(letra)
