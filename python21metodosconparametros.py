## METODOS CON PARAMETROS
def saludo(nombre):
    print("Bienvenido Mr/Mrs" " " + nombre)

def despedida (nombre, dia):
    print("Ha sido un placer hoy " + dia + ", Mr/Mrs " + nombre)

# Programa principal
print ("EJEMPLO METODOS CON PARAMETROS")
print ("Introduce tu nombre")
name = input()
print ("Introduce la fecha de hoy")
day = input()
name = name.upper()
saludo(name)
despedida(name, day)
print("FIN DE PROGRAMA")
