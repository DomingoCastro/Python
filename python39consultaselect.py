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
# TENEMOS UNA CONEXION ABIERTA, PODEMOS REALIZAR CONSULTAS
# CREAMOS UN CURSOR PARA REALIZAR UNA CONSULTA
cursor = conexion.cursor()
# EL CURSOR MANEJA TANTO CONSULTAS DE SELECCION COMO CONSULTAS DE ACCION
# CREAMOS NUESTRA CONSULTA SELECT
sql = "SELECT * from DEPT"
# EL CURSOR ES EL ENCARGADO DE EJECUTAR LA CONSULTA
cursor.execute(sql)
#TENEMOS DATOS DE LOS DEPARTAMENTOS, PODEMOS LEER FILA A FILA CADA UNO DE LOS DATOS CON EL METODO fetchone()
# DICHO METODO, CADA VEZ QUE SE EJECUTA, SE MUEVE UNA FILA EN EL CURSOR
# DIBUJAMOS LA FILA ACTUAL
# CADA VEZ QUE EJECUTAMOS FETCHONE SE MUEVE UNA FILA
for row in cursor:
    numero = str(row.DEPT_NO)
    nombre = str(row.DNOMBRE)
    localidad = str(row.LOC)
    print(numero +", Nombre: " + nombre + ", Localidad: " +  localidad)
    # print(row)
    # TAMBIEN PÒDEMOS DIBUJAR DE FORMA DINAMICA LA COLUMNA
    print(row.LOC)
# CERRAMOS LA CONEXION y el cursor
# EL CURSOR SOLO SE PUEDE RECORRER UNA VEZ NO PUEDE VOLVER ATRÁS
cursor.close()
conexion.close()
print("FIN DEL PROGRAMA")