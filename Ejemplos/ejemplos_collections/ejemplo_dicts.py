"""
Ejemplos de uso de diccionarios
"""
autores = ["Pedro Picapiedra", "Pablo Mármol"]
# Crear un nuevo dict
libro = {
    "autor": autores,
    "titulo": "Los picapiedra",
    "anno": -10000
}
# print(libro)

# Acceder al valor de una llave
# print(libro["titulo"])

# Averiguar las llaves de un dict
# print(libro.keys())

# libro["genero"] = "Novela"
# print(libro.keys())

# # Averiguar los valores de un dict
# print(libro.values())

# # Averiguar los items de un dict
# print(libro.items())

# # Cambiar un valor
libro["genero"] = "fantasia"
print(libro)
# libro.update({"genero": "epica"})
# print(libro)

# Eliminar un elemento
libro.pop("genero")
print(libro)