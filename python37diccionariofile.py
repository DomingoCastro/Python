import json
print("DOCUMENTO JSON DICCIONARIOS")
file = open("JSON/jugadores_nokey.json", "r")

# PARA TRANSFORMAR LOS DATOS JSON EN FORMATO DICCIONARIO
# SE UTILIZA EL METODO LOAD()
data = json.load(file);
for jugador in data:
    print(jugador["nombre"])
file.close()
# PONGAMOS QUE DESEAMOS AÑADIR NUEVOS ELEMENTOS A NUESTRO DICCIONARIO
# PARA CREAR NUEVOS OBJETOS SE UTILIZA EL METODO APPEND
# UN OBJETO DICCIONARIO SE CREA MENDIANTE LLAVES
newPlayer =  {
    "numero": 99,
    "nombre": "Paquito Chocolatero",
    "posicion": "Aguador",
    "imagen": ""
}
#AÑADIMOS AL DICCIONARIO UN NUEVO ELEMENTO
data.append(newPlayer)
# UNA VEZ QUE TENEMOS LOS DATOS EN data
# DEBEMOS VOLVER A ESCRIBIRLOS EN EL ARCHIVO
# EN FORAMTO JSON STRING
# DEBEMOS CONVERTIR LA COLECCION DICCIONARIO EN STRING
jsonString = json.dumps(data)
# ABRIMOS EL FICHERO EN MODO ESCRITURA
file = open("JSON/jugadores_nokey.json", "w+")
file.write(jsonString)
file.flush()
file.close()
print("FIN DE PROGRAMA")