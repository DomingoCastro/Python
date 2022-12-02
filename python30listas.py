# Declaramos una lista.
# Esta variable la vamos a utilizar en el programa principal
# Y tambien en los metodos
nombres = ["Adri", "Domi", "Angel", "Carlos", "Alex", "Jose", "Sara", "Adri"]

def mostrarNombres():
    # Aqui vamos a dibujar los nombres con un bucle de referencia
    # for name in nombres:
    #     print(name)
    #Lo hacemos con un bucle contador porque quiero visualizar las posicioens de cada nombre
    for i in range(len(nombres)):
        name = nombres[i]
        print(str(i) + ".- " + name)

print("Ejemplo de listas python")
#Añadimos un nuevo nombre
# nombres.append("El nuevo")
# Insertamos un elemento en medio
# nombres.insert(2, "El del medio")
# Eliminamos utilizando REMOVE (Este borrara el primer ADRI que encuentra)
# nombres.remove("Adri")
# Eliminamos utilizando Pop (Este borra el indice que digamos) (EN ESTE CASO BORRA EL ULTIMO ADRI)
# nombres.pop(7)
# mostrarNombres()
print("Lista de numeros enteros")
numeros = [20,4,15,122,56,12,6,2]
# Ordena los numeros en forma ascendente
# numeros.sort()
# Numeros descendentes:
numeros.sort( reverse = True)
for num in numeros:
    print(num)
print("FIN DE PROGRAMA")