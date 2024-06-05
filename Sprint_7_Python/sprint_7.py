

















# Crear una lista de claves del diccionario original
lista_claves = list(random_dict.keys())
lista_value = list(random_dict.values())
print("Lista de claves del diccionario:\n", lista_claves)
print("Lista de values del diccionario:\n", lista_value)





print('hola mundo')


def invertir(random_dict):
    inverso = {v: k for k, v in random_dict.items()}
    return inverso
inverso_nivel_1 = invertir(random_dict)
print("Diccionarios inverso:\n" , inverso_nivel_1 ) , print("N elementos:\n" , len(inverso_nivel_1) )



# Diccionario inveso con duplicados

def inverso_amb_duplicats(dictionary):
    invers_dict = {}
    for k, v in dictionary.items():
        if v in invers_dict:
            if isinstance(invers_dict[v], list):
                invers_dict[v].append(k)
            else:
                invers_dict[v] = [invers_dict[v], k]
        else:
            invers_dict[v] = k
    return invers_dict

# Prueba 1: Diccionario con valores unicos.
dictionary = {"a": 1, "b": 2, "c": 3}
print("Diccionario original:", dictionary)
resultado = inverso_amb_duplicats(dictionary)
print("Diccionario invertido:", resultado)

# Prueba 2: Diccionario con valores duplicados.
dictionary = {"x": "apple", "y": "banana", "z": "banana", "w": "apple"}
print("Diccionario original:", dictionary)
resultado = inverso_amb_duplicats(dictionary)
print("Diccionario invertido:", resultado)
