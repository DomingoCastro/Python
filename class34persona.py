class Persona:
    nombre = ""
    apellidos = ""
    email = ""
    anyo = 0
    pais = "Lo que sea..."

    # EL CONSTRUCTOR ES UN METODO PARA INICIAR 
    # LOS VALORES DE LAS PROPIEDADES DE LA CLASE
    # Por ejemplo, pongamos que queremos que cualquier
    # persona, al crearla sea de un pais: PORTUGAL
    def __init__(self):
        self.pais = "Portugal"

    # METODO PARA PERSONALIZAR EL DIBUJO DE LA CLASE
    def __str__(self):
        return self.apellidos + " " + self.nombre + ", Pais: " + self.pais


    # METODO PARA RECUPERAR LOS DATOS
    # COMPLETOS DE UNA PERSONA
    def getNombreCompelto(self):
        return self.nombre + " " + self.apellidos
    
    # Metodos para que nos devuelva la edad
    def getEdad(self):
        return 2022 - self.anyo

    def getDescripcion(self, descripcion):
        return self.getNombreCompelto() + ", " + descripcion