# CICLOS, BUCLES O LOOPS

# WHILE

# # Imprimir todos los números del 0 al 6
# i = 1
# while i <= 6:
#   print(i)
#   i += 1 # i = i + 1

# # Imprimir todos los números del 1 al 6 pero parar si pasa por 3
# i = 1
# while i <= 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# # Imprimir todos los números del 1 al 6 pero saltarse el 3
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# # OPCIONAL: else cuando se rompe la condición
# i = 1
# while i <= 6:
#   print(i)
#   i += 1
# else:
#   print("i ya no es menor que 6")

# # FOR

# # Para iterar en una colección
# frutas = ["manzana", "banano", "cereza"]
# for fruta in frutas:
#   print(fruta)

# # Break para parar antes
# frutas = ["manzana", "banano", "cereza"]
# for fruta in frutas:
#   if fruta == "banano":
#     continue
#   print(fruta)

# # Para iterar una cantidad N de veces
# for i in range(6):
#   print(i+1)

# # iterando de 2 en 2
# for i in range(0,6,2): # [0, 6[
#   print("seis 2.0")

 # For anidados
frutas = ["manzana", "sandía", "cereza"]
adjetivos = ["roja", "grande", "sabrosa"]

for fruta in frutas:
  for adj in adjetivos:
    print(fruta, adj)
