import pyodbc

print("Primera consulta SELECT python")
servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "SA"
password = ""
# CREAMOS NUESTRA CADENA DE CONEXION
connectionString=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
# conectamos nuestra BBDD
print ("Intentando conectar...")
conexion = pyodbc.connect(connectionString)
print("Conectado a SQL SERVER")
# VAMOS A PEDIR LOS DATOS AL USUARIO Y LOS UTILIZAREMOS PARA CONCATENAR Y REALIZAR NUESTRA CONSULTA INSERT
print("Introduzca un numero de departamento")
numero= input()
print("Introduzca el nombre del departamento")
nombre = input()
print ("Introduzca la localidad")
localidad = input()
sql= "insert into dept values (66, 'PYTHON', 'ALMERIA')"
# EJECUTAMOS LA CONSULTA
cursor= conexion.cursor()
cursor.execute(sql)
# CUANDO EJECUTAMOS CONSULTAS DE ACCION PARA AVERIGUAR EL NUMERO DE REGISTROS QUE HAN SIDO AFECTADOS POR LA CONSULTA SE UTILIZA
# LA PROPIEDAD rowcount DEL CURSOR
filasInsertadas = cursor.rowcount
print ("RowCount: " + str(filasInsertadas))
# EN PYTHON, LAS CONSULTAS DE ACCION SE REALIZAN DE FORMA TEMPORAL, ES DECIR, NO SON LLEVADAS A LA BASE DE DATOS HASTA QUE NO SE LO DECIMOS
# MEDIANTE EL METODO COMMIT() DEL CURSOR
cursor.commit()
# CON ROLLBACK LE INDICAMOS QUE DESHAGA LOS CAMBIOS
# cursor.rollback()
cursor.close()
conexion.close()
print("FIN DE PROGRAMA")