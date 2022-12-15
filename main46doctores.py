from conexion46doctores import ConexionDoctores
from class46doctores import Doctores
connection= ConexionDoctores()
print("Elige una opcion entre 1-5 o escriba 0 para salir")
print("0.- Salir del programa")
print("1.- Insertar un Doctor")
print("2.- Eliminar un Doctor")
print("3.- Buscar Doctor por especialidad")
print("4.- Modificar salario de doctor")
print("5.- Mostrar todos los doctores")
opcion= int(input())
if opcion == 1:
    print("Escribe el código del hospital")
    print("Mostrando hospitales")
    hospi= connection.MostrarHospitales()
    for hospital in hospi:
        print(str(hospital.hospital_cod)+ "/"+ hospital.nombre)
    codigo = input()
    # print("Escribe el numero del doctor")
    # numero = input()
    print("Escribe el apellido")
    apellido = input()
    print("Escribe la especialidad")
    especialidad= input()
    print("Escribe el salario")
    salario= input()
    respuesta= connection.InsertarDoctores(codigo,apellido,especialidad,salario)
    print("Doctor inscrito en la base de datos: " + str(respuesta))
elif opcion == 2:
    print("Escribe el numero del doctor")
    numero= input()
    respuesta=connection.EliminarDoctores(numero)
    print("Se a eliminado al doctor: " + str(respuesta))
elif opcion == 3:
    print("Escribe la especialidad")
    especialidad= input()
    espec=connection.BuscarDoctores(especialidad)
    if (not espec):
        print("No existe doctor con esa especialidad")
    else:
        print("Los doctores que pertenecen a esa especialidad son: " + "Numero de doctor: "+ str(espec.numero) + "Apellido: " + espec.apellido + "Especialidad: " + espec.especialidad)
elif opcion == 4:
    print("Escribe el salario a modificar")
    salario= input()
    print("Escribe el ID del doctor")
    numero = input()
    respuesta= connection.IncrementoSalarial(salario,numero)
    print("El salario fue modificado al doctor: " + str(respuesta))
elif opcion == 5:
    print("Mostrando todos los doctores")
    print("---------------------------")
    print("COD_HOSPITAL/DOCTOR_NO/APELLIDO/ESPECIALIDAD/SALARIO")
    print("--------------------------------------------------")
    doctors= connection.MostrarDoctores()
    for doctores in doctors:
        print(str(doctores.hospital)+ "/"+ str(doctores.numero) + "/" +doctores.apellido + "/"+ doctores.especialidad+ "/" + str(doctores.salario))
elif opcion == 0:
    print("CERRANDO PROGRAMA...")
else:
    print("ERROR, NUMERO INCORRECTO")
print("FIN DE PROGRAMA")
