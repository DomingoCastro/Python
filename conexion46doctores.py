import pyodbc
from class46doctores import Doctores, Hospitales

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "SA"
password = ""

class ConexionDoctores:
    def __init__(self):
        connectionString=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
        self.conexion = pyodbc.connect(connectionString)

    def InsertarDoctores(self, codigo, apellido, especialidad, salario):
        cursor= self.conexion.cursor()
        sql = "INSERT INTO DOCTOR VALUES (?,(select MAX (DOCTOR_NO) from DOCTOR) + 1,?,?,?)"
        cursor.execute(sql,(codigo,apellido,especialidad,salario))
        cursor.commit()
        insertados= cursor.rowcount
        cursor.close()
        return insertados
    def EliminarDoctores(self, numero):
        cursor = self.conexion.cursor()
        sql = "DELETE FROM DOCTOR WHERE DOCTOR_NO=?"
        cursor.execute(sql,(numero))
        cursor.commit()
        borrados= cursor.rowcount
        cursor.close()
        return borrados
    def BuscarDoctores(self, especialidad):
        cursor= self.conexion.cursor()
        sql = "SELECT * FROM DOCTOR WHERE ESPECIALIDAD=?"
        cursor.execute(sql,(especialidad))
        row= cursor.fetchone()
        if (not row):
            cursor.close()
            return None
        else:
            doctor = Doctores()
            doctor.numero = row.DOCTOR_NO
            doctor.apellido = row.APELLIDO
            doctor.especialidad = row.ESPECIALIDAD
            return doctor
    def IncrementoSalarial(self, salario, numero):
        cursor = self.conexion.cursor()
        sql = "UPDATE DOCTOR SET SALARIO=? WHERE DOCTOR_NO=?"
        cursor.execute(sql,(salario,numero))
        cursor.commit()
        modificados= cursor.rowcount
        cursor.close()
        return modificados
    def MostrarDoctores(self):
        cursor= self.conexion.cursor()
        sql= "SELECT * FROM DOCTOR"
        cursor.execute(sql)
        doctors=[]
        row= cursor.fetchone()
        for row in cursor:
            doc=Doctores()
            doc.hospital= row.HOSPITAL_COD
            doc.numero= row.DOCTOR_NO
            doc.apellido= row.APELLIDO
            doc.especialidad= row.ESPECIALIDAD
            doc.salario= row.SALARIO
            doctors.append(doc)
        cursor.close()
        return doctors
    def MostrarHospitales(self):
        cursor= self.conexion.cursor()
        sql = "SELECT HOSPITAL_COD, NOMBRE FROM HOSPITAL"
        cursor.execute(sql)
        hospitales= []
        row= cursor.fetchone()
        for row in cursor:
            hosp= Hospitales()
            hosp.hospital_cod = row.HOSPITAL_COD
            hosp.nombre= row.NOMBRE
            hospitales.append(hosp)
        cursor.close()
        return hospitales
