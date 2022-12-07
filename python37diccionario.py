import json
print("Ejemplo diccionarios Python")
# La variable data es un diccionario de JSON
data = {

    'employees' : [
        {
            'name' : 'John Doe',
            'department' : 'Marketing',
            'place' : 'Remote'
        },
        {
            'name' : 'Jane Doe',
            'department' : 'Software Engineering',
            'place' : 'Remote'
        },
        {
            'name' : 'Don Joe',
            'department' : 'Software Engineering',
            'place' : 'Office'
        }
    ]
}

# SI DESEAMOS REALIZAR UN PRINT DE UN DICCIONARIO
# DEBEMOS CONVERTIRLO A STRING, DUMP()
jsonString = json.dumps(data)
print(jsonString)
# SI DESEAMOS RECORRER O RECUPERAR ELEMENTOS DENTRO DEL DICCIONARIO
# DEBEMOS RECORRER DATA, YA QUE ES COMO UNA LISTA/COLECCION
for elemento in data['employees']:
    print(elemento["name"])