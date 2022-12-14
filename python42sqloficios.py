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
print("OFICIO QUE DESEA CAMBIAR")
oficio = input()
print("SALARIO A AUMENTAR")
salario = input()
# update EMP set SALARIO= SALARIO + 1 WHERE OFICIO = 'EMPLEADO'
cursor = conexion.cursor()
sql = "update EMP set SALARIO=SALARIO + ? WHERE OFICIO =?"
cursor.execute(sql,(salario, oficio))
cursor.commit()
filasInsertadas = cursor.rowcount
print("--------CANTIDAD DE FILAS MODIFICADAS--------")
print("Filas modificadas = " + str(filasInsertadas))
print("--------REALIZANDO ACCIONES Y CONSULTAS... --------")
cursor.close()
cursor = conexion.cursor()
sql2 = "select APELLIDO, SALARIO, OFICIO FROM EMP WHERE OFICIO= ?"
cursor.execute(sql2,(oficio))
print("--------SALARIOS MODIFICADOS--------")
for row in cursor:
    print(row.APELLIDO + ", " + row.OFICIO + ", " +str(row.SALARIO))
print("--------FIN DE LAS MODIFICACIONES--------")
cursor.close()
conexion.close()
print ("FIN DE PROGRAMA")