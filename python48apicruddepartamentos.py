import requests
import json

print("Ejemplo api Crud Departamentos")
url= "https://apicruddepartamentoscore.azurewebsites.net/"
print("1.- Mostrar departamentos")
print("2.- Insertar departamento")
print("3.- Modificar departamento")
print("4.- Eliminar departamento")
opcion = int(input())
if opcion == 1:
    peticion = "api/departamentos"
    response = requests.get(url + peticion)
    departamentos =  response.json()
    for dept in departamentos:
        print(str(dept["numero"]) + ", " + dept["nombre"] + ", " + dept["localidad"])
elif opcion == 2:
    print("Nuevo departamento")
    print("Introduzca ID Departamento")
    numero = int(input())
    print("Introduzca un nombre")
    nombre = input()
    print("Introduce la localidad")
    loc= input()
    peticion = "api/departamentos"
    departamento= {
        "numero": numero,
        "nombre": nombre,
        "localidad": loc
    }

    response= requests.post(url + peticion,  json=departamento)
    print("Status " + str(response.status_code))
elif opcion == 3:
    print("Que departamento deseas modificar?")
    numero= int(input())
    print("Que nombre deseas ponerle?")
    nombre = input()
    print("Localidad que desea poner")
    localidad= input()
    peticion = "api/departamentos"
    departamento={
        "numero": numero,
        "nombre": nombre,
        "localidad": localidad
    }
    response= requests.put(url + peticion, json=departamento)
    print("Status " + str(response.status_code))
elif opcion == 4:
    print("ID Departamento a eliminar")
    numero= input()
    peticion = "api/departamentos/" + numero
    response= requests.delete(url + peticion)
    print("Status: " + str(response.status_code))
else:
    print("opcion incorrecta")
print("FIN DE PROGRAMA")