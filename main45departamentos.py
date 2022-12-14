from conexion45departamentos import ConexionDepartamentos
from class45departamentos import Departamento
connection= ConexionDepartamentos()
print("Elige una opcion (1-3), si desea salir escriba 0")
print("0.- Salir del programa")
print("1.- Inscribir un nuevo departamento")
print("2.- Borrar un departamento")
print("3.- Modificar un departamento")
print("4.- Buscar departamento")
opcion= int(input())
if opcion == 1:
    print("Escribe un numero")
    numero = input()
    print("Escribe un nombre")
    nombre = input()
    print("Escribe la localidad")
    localidad = input()
    respuesta= connection.InsertarDepartamento(numero,nombre,localidad)
    print("Departamento inscrito: " + str(respuesta))
elif opcion == 2:
    print("Escribe el numero del departamento que desea eliminar")
    numero = input()
    respuesta= connection.EliminarDepartamento(numero)
    print("Departamento eliminado: " + str(respuesta))
elif opcion == 3:
    print("Escribe un nombre")
    nombre= input()
    print("Escribe la localidad")
    localidad= input()
    print("Escribe el numero de departamento que desea modificar")
    numero= input()
    respuesta= connection.ModificarDepartamento(nombre,localidad,numero)
    print("Se ha modificado el departamento: " + str(respuesta))
elif opcion == 4:
    print("¿Que departamento desea buscar? (Numero)")
    numero = input()
    dept= connection.BuscarDepartamento(numero)
    if (not dept):
        print("No existe departamento con ese numero")
    else:
        print("El departamento que has buscado es: " + dept.nombre + ", " + dept.localidad)
elif opcion == 0:
    print("CERRANDO PROGRAMA...")
else:
    print("ERROR, NUMERO NO ADMITIDO CERRANDO PROGRAMA.")
print("FIN DE PROGRAMA")
