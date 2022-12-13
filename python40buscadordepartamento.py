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
# PEDIMOS AL USUARIO EL NUMERO DEL DEPARTAMENTO 
print("Introduzca el numero del departamento")
# EL USUARIO NOS DA UN NUMERO QUE NOSOTROS VAMOS A UTILIZAR PARA CONCATENAR A LA CONSULTA, AUNQUE SEA UN NUMERO, ES UN DATO STRING
data = input()
sql = "select * from dept where DEPT_NO = " + data
# SOLAMENTE DEVOLVERA UNA FILA YA QUE BUSCAMOS POR ID
cursor = conexion.execute(sql)
row = cursor.fetchone()
    # para preguntar si hay un dato en la fila se utiliza el operador not
if (not row):
    print ("No existe ese departamento")
else:
    print(row.DNOMBRE + ", Localidad: " + row.LOC)
cursor.close()
conexion.close()
print ("FIN DE PROGRAMA")