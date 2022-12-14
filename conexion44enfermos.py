import pyodbc


servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "SA"
password = ""

class ConexionEnfermos:
    # EN EL INICIO DE LA CLASE DEBEMOS CREAR UN OBJETO CONEXION PARA UTILIZARLO EN TODOS LOS METODOS
    def __init__(self):
        # SELF ES LA CLASE EN LA QUE ESTAMOS TRABJAANDO Y NOS VAMOS A CREAR UNA PROPIEDAD PARA TENER LA CONEXION
        connectionString=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
        self.conexion = pyodbc.connect(connectionString)
    # TENDREMOS UN METODO PARA ELIMINAR UN ENFERMO POR INSCRIPCION
    def elmininarEnfermo(self, inscripcion):
        #CREAR CURSOR, EJECUTAR Y CERRAR
        cursor = self.conexion.cursor()
        sqldelete= "delete from ENFERMO where INSCRIPCION=?"
        cursor.execute(sqldelete,(inscripcion))
        eliminados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminados

    def modificarEnfermo(self, apellido, inscripcion):
        cursor = self.conexion.cursor()
        sqlmod = "UPDATE ENFERMO SET APELLIDO=? WHERE INSCRIPCION=?"
        cursor.execute(sqlmod,(apellido, inscripcion))
        modificados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return modificados        