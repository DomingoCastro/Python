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
