print("Escribe tu email")
email = input()
print(email.find("@"))
findarroba = email.find("@")
findpunto = email.find(".")
print(email.find("."))
print(email.startswith("@" or "."))
tiene = (email.find("@") == -1 or (email.find(".")) == -1 )
unpuntoyarroba = email.count("@") and email.count(".")
dominio = email[email.rfind("."):]
print(tiene)
if (email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith(".")):
    print("ERROR NO PUEDES PONER @ Y . AL INICIO NI AL FINAL")
elif tiene == "true" :
    print("ERROR, NO CONTIENE @ O .")
elif unpuntoyarroba != 1:
    print("SOLO PUEDES PONER 1 , Y UN @")
elif len(dominio) < 2 and len(dominio) > 4:
    print("EL DOMINIO .COM .ES O SIMILAR NO PUEDE SER INFERIOR A 2 NI SUPERIOR A 4")
elif findarroba > findpunto:
    print("DELANTE DEL .COM .ES O SIMILAR DEBE ESTAR @")
elif "@" and "." not in email:
    print ("DEBE TEBER UN @ Y UN .")
else:
    print("CUENTA CREADA CON EXITO")
