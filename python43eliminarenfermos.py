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
cursor = conexion.cursor()
sqlselect= "SELECT * FROM ENFERMO"
cursor.execute(sqlselect)
print("--------- Listado de enfermos---------")
for row in cursor:
    print(row.INSCRIPCION+ ", "+ row.APELLIDO)
cursor.close()
print("Esta es la lista de enfermos, cual desea eliminar? (PONGA EL NUMERO DE INSCRIPCION")
inscripcion = input()
cursor = conexion.cursor()
sqldelete= "delete from ENFERMO where INSCRIPCION=?"
cursor.execute(sqldelete,(inscripcion))
cursor.commit()
filasEjecutadas= cursor.rowcount
print("Se ha eliminado un total de: " + str(filasEjecutadas) + "pacientes")
cursor.close()
conexion.close()
print("FIN DE PROGRAMA")