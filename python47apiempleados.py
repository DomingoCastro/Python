import requests
import json

url = "https://apiempleadosspgs.azurewebsites.net/"
print("1.- Todos los empleados")
print("2.- Buscar empleado")
print("Seleccione una opcion")
opcion= int(input())
if opcion == 1:
    peticion = "api/empleados"
    # REALIZAMOS UNA PETICION GET Y CAPTURAMOS LA RESPUESTA
    response = requests.get(url + peticion)
    # CONVERTIMOS LA RESPUESTA A DICCIONARIO JSON
    empleados = response.json()
    # UN DICCIONARIO PODEMOS RECORRERLO SI ES UN COJUNTO
    print("LISTADO EMPLEADOS API")
    for emp in empleados:
        print(emp)
elif opcion == 2:
    print("Introduce el ID del empleado")
    idempleado= input()
    peticion = "api/empleados/" + idempleado
    response = requests.get(url+peticion) 
    empleados = response.json()
    print("Lista empleados")
    print(empleados["apellido"] + ", " + empleados["oficio"] + ", " + str(empleados["salario"]))
else:
    print("ERROR")

print("FIN DE PROGRAMA")