"""
Ejemplos de uso de tuplas
"""
# Crear una nueva tupla
tupla_series = ["The Sopranos", "Breaking Bad", "Game of Thrones", "Pasión de Gavilanes"]
print(tupla_series)

# Las tuplas están indexadas por lo que se accede a sus elementos igual que una lista
print("Primer elemento: {}".format(tupla_series[0]))

# Checkear si existe un elemento
if "Breaking Bad" in tupla_series:
    print("Breaking Bad está en la tupla")

# Agregar una tupla a otra
nuevas_series = ("The Last of Us",)
tupla_series += nuevas_series
print(tupla_series)

# Desempacar tuplas
config = ("Arturo", "Zamora", 1995)
(nombre, apellido, anno_nacimiento) = config
print(nombre)
print(apellido)
print(anno_nacimiento)

# Desempacar con asterisco
config = ("Arturo", "Zamora", 1995, "correo@correo.com")
(nombre, apellido, *el_resto) = config
print(nombre)
print(apellido)
print(el_resto)

