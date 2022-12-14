import pyodbc
from class45departamentos import Departamento

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "SA"
password = ""

class ConexionDepartamentos:
    def __init__(self): 
        connectionString=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
        self.conexion = pyodbc.connect(connectionString)
    def InsertarDepartamento(self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        # insert into dept values (120, 'COOLMOD', 'VALENCIA')
        sql= "insert into dept values (?, ?, ?)"
        cursor.execute(sql,(numero, nombre, localidad))
        insertados= cursor.rowcount
        cursor.commit()
        cursor.close()
        return insertados
    def EliminarDepartamento(self, numero):
        cursor = self.conexion.cursor()
        sql= "DELETE FROM DEPT WHERE DEPT_NO=?"
        cursor.execute(sql,(numero))
        eliminados= cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminados
    def ModificarDepartamento(self,nombre, localidad, numero):
        cursor= self.conexion.cursor()
        sql= "UPDATE DEPT SET dNOMBRE=?, LOC=? WHERE DEPT_NO=?"
        cursor.execute(sql,(nombre,localidad,numero))
        modificados= cursor.rowcount
        cursor.commit()
        cursor.close()
        return modificados
    def BuscarDepartamento(self, numero):
        cursor= self.conexion.cursor()
        sql = "SELECT * FROM DEPT WHERE DEPT_NO=?"
        cursor.execute(sql,(numero))
        row = cursor.fetchone()
        if (not row):
            cursor.close()
            return None
        else:
            dept = Departamento()
            dept.numero = row.DEPT_NO
            dept.nombre = row.DNOMBRE
            dept.localidad = row.LOC
            return dept