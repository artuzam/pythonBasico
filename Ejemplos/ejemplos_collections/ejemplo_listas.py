"""
Ejemplos de uso de listas
"""
# Crear una nueva lista
lista_autos = ["Audi", "Porsche", "Mercedes-Benz", "Toyota"]
# print(lista_autos)

# Averiguar el largo de una lista
# print(len(lista_autos))

# Los elementos de una lista están indexados
# print("El primer elemento de la lista es: {}".format(
#     lista_autos[0]
# ))

# print("El último elemento de la lista es: {}".format(
#     lista_autos[-1]
# ))

# print("Los elementos entre en segundo y el cuarto (no incluido) son: {0}".format(
#     lista_autos[1:4], # [1 ,4[
# ))

# # modificar elementos de la lista
# lista_autos[1] = "Subaru"
# print(lista_autos)

# # modificar elementos en un rango
# lista_autos[0:2] = ["Tesla", "Renault"]
# print(lista_autos)

# # Añadir elementos
# lista_autos.append("Suzuki")
# lista_autos.insert(2, "Nissan")
# print(lista_autos)

# # Añadir otra lista (o cualquier otro iterable)
# autos_chinos = ["Geely", "Changan"]
# lista_autos.extend(autos_chinos)
# print(lista_autos)

# Eliminar un elemento
# if "Tesla" in lista_autos:
#     lista_autos.remove("Tesla")
# print(lista_autos)

# # Eliminar por índice
# lista_autos.pop(0) #elimina el primer elemento
# print(lista_autos)

# Eliminar el último
# lista_autos.pop()
# print(lista_autos)

# # Filtrado SIN List comprehension
# autos_con_a = []

# for auto in lista_autos:
#   if "a" in auto:
#     autos_con_a.append(auto)
# print(autos_con_a)

# # List comprehension (2)
# autos_con_a = [auto for auto in lista_autos if "a" in auto]
# print(autos_con_a)
# autos_sin_a_upper = [auto.upper() for auto in lista_autos if "a" not in auto]
# print(autos_sin_a_upper)

# # Las listas se pueden ordenar de forma alfabética o numérica
# # ordenar lista ascendente
# lista_autos.sort()
# print(lista_autos)

# # ordenar lista descendente
# lista_autos.sort(reverse = True)
# print(lista_autos)

# # copiar listas
# nueva_lista = lista_autos
# nueva_lista_1 = lista_autos.copy()
# lista_autos[0] = "Dodge"
# print("Lista copiada mal:")
# print(nueva_lista)
# print("Lista copiada bien:")
# print(nueva_lista_1)

# # Vaciar la lista
# lista_autos.clear()
# print(lista_autos)
