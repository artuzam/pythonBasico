"""
Ejemplos de uso de diccionarios
"""
# Crear un nuevo dict
dict_ejemplo = {
    "autor": "J.K Rowling",
    "titulo": "Harry Potter",
    "anno": 1993
}
print(dict_ejemplo)

# Acceder al valor de una llave
print(dict_ejemplo["titulo"])

# Averiguar las llaves de un dict
print(dict_ejemplo.keys())

dict_ejemplo["genero"] = "Novela"
print(dict_ejemplo.keys())

# Averiguar los valores de un dict
print(dict_ejemplo.values())

# Averiguar los items de un dict
print(dict_ejemplo.items())

# Cambiar un valor
dict_ejemplo["genero"] = "fantasia"
print(dict_ejemplo)
dict_ejemplo.update("genero", "novela")
print(dict_ejemplo)

# Eliminar un elemento
dict_ejemplo.pop("genero")
print(dict_ejemplo)