
# CON * IMPORTA TODOS LOS METODOS DE LA PAGINA PYTHON24 PARA COPIAR SOLO ALGUNOS PONER EL NOMBRE EN VEZ DE *
from python24funcionesmatematicas import *
resultado = 0
pregunta = "s"
while pregunta == "s":
    abrirMenu()
    opcion = int(input())
    print("Escribe un numero")
    numero1= int(input())
    print("Escribe otro numero")
    numero2 = int(input())
    if opcion == 1:
        resultado = numero1 + numero2
        print("El resultado de la suma es: " + str(resultado))
    elif opcion == 2:
        resultado = numero1 - numero2
        print("El resultado de la resta es: " + str(resultado))
    elif opcion == 3:
        resultado = numero1 / numero2
        print("El resultado de la division es: " + str(resultado))
    elif opcion == 4:
        resultado = numero1 * numero2
        print("El resultado de la multiplicación es: " + str(resultado))
    elif opcion == 0:
        print("Gracias por utilizar este menu")
        pregunta = "no"
    
    print("Desea volver a poner otros numeros? s/n")
    pregunta = (input())
    if pregunta == "n":
        print("Gracias por usar el programa")
print ("FIN DE PROGRAMA")
print ("Pulsa una tecla para cerrar el programa")
input()