def abrirMenu():
    print("SELECCIONE UNA OPCION")
    print("0.- Salir")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Dividir")
    print("4.- Multiplicar")

def operacion(numero1, numero2, opcion):
    if opcion == 1:
        return numero1 + numero2
    elif opcion == 2:
        return numero1 - numero2
    elif opcion == 3:
        return numero1 / numero2
    elif opcion == 4:
        return numero1 * numero2