# IMPORTAMOS LA CLASE PERSONA PARA TRABAJAR CON ELLA
from class34persona import Persona

print("Ejmplo clases persona")

# INSTANCIAMOS UN OBJETO DE LA CLASE PERSONAS

person = Persona()

# Podemos cambiar la propiedad una vez creado el objeto

person.pais = "España"
print("Pais : " + person.pais)

#INCLUIMOS DATOS PARA LA PERSONA

person.nombre = "Paco"
person.apellidos = "Python"
person.email = "Email@gmail.com"
person.anyo = 1987

# llamamos a los objetos

print("Nombre completo de persona 1: " + "\n" + person.getNombreCompelto())
print("Edad: " + str(person.getEdad()))
print("-------------------")
print(person)
print(person.getDescripcion("Rubio ojos verdes"))
print("-------------------")
# CREAMOS OTRO OBJETO Y LO VEMOS TAMBIEN

person2 = Persona()


print("Pais persona 2: " + person2.pais)
print("FIN DE PROGRAMA")