from math import trunc
def isbn():
    print("Danos tu ISBN (10 CARACTERES)")
    aux = input()
    suma = 0
    longitud = len(aux)
    while (aux.isdigit() == False):
        print("Danos tu ISBN CORRECTO  (SOLO NUMEROS)")
        aux = input()
    if longitud < 10 or longitud != 10 :
            print("DEBE TENER 10 CARACTERES")
    else:
        for i in range(longitud):
            letra = aux[i]
            numero = int(letra)
            posicion = i + 1
            operacion = numero * posicion
            suma = suma + operacion
        if (suma % 11 == 0):
            print("Numero correcto")
        else:
            print ("Numero ISBN incorrecto")
    print ("FIN DE PROGRAMA")

def abrirMenuTools():
    print("SELECCIONE UNA OPCION")
    print("0.- Salir")
    print("1.- ISBN")
    print("2.- Email")
    print("3.- NIF")

def nif():
    print("Escribe tu DNI")
    dni = (input())
    if (dni.isdigit() == False):
        print("DEBE SER SOLO NUMEROS")
    elif len(dni) != 8 :
        print ("DEBE TENER 8 CARACTERES")
    else:
        dni = int(dni)
        operacion = (dni - (trunc(dni / 23) * 23))
        cadena = "TRWAGMYFPDXBNJZSQVHLCKET" 
        letra = cadena[operacion]
        print("Su letra del dni es " + letra)

def email():
    print("Escribe tu email")
    email = input()
    findarroba = email.find("@")
    findpunto = email.find(".")
    unpuntoyarroba = email.count("@") and email.count(".")
    ultimoPunto = email.rfind(".")
    dominio = email[ultimoPunto + 1:]
    longituddominio = len(dominio)
    if (email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith(".")):
        print("ERROR NO PUEDES PONER @ Y . AL INICIO NI AL FINAL")
    elif email.find("@") == -1 or (email.find(".")) == -1 :
        print("ERROR, NO CONTIENE @ O .")
    elif email.count("@") != 1 or email.count(".") != 1:
        print("SOLO PUEDES PONER 1 , Y UN @")
    elif findarroba > findpunto:
        print("DELANTE DEL .COM .ES O SIMILAR DEBE ESTAR @")
    elif "@" and "." not in email:
        print ("DEBE TEBER UN @ Y UN .")
    else:
        if  longituddominio >= 2 and longituddominio <= 4:
         print("CUENTA CREADA CON EXITO")
        else:

            print("EL DOMINIO .COM .ES O SIMILAR NO PUEDE SER INFERIOR A 2 NI SUPERIOR A 4")
    print("FIN PROGRAMA")