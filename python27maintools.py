from python26funcionestools import *

print("Elige que deseas hacer")
abrirMenuTools()
opcion = (int(input()))
if opcion == 1:
    isbn()
elif opcion == 2:
    email()
elif opcion == 3:
    nif()
else:
    print("Esa opcion no es valida")