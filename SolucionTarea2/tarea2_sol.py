# Factorial de un numero num
def calcular_factorial(num):
    if num < 0:
        return "El factorial de un negativo no existe"
    elif num == 0:
        return 1
    else:
      factorial = 1
      for i in range(1, num+1):
          factorial = factorial * i
    return factorial

# num = int(input("Ingrese un numero mayor o igual a 0: \n"))
# print(calcular_factorial(num))

# triangulo de N niveles
def dibujar_triangulo(n):
    if n <= 0:
        print("El numero debe ser mayor a 0")
        return
    triangulo = ""
    for i in range(1, n+1):
        triangulo += str(i) + " "
        print(triangulo)
# n = int(input("Ingrese un numero mayor 0: \n"))
# dibujar_triangulo(n)

# strings intercaladas
def intercalar_strings(str1, str2):
    if len(str1) != len(str2):
        return "Las strings deben ser del mismo largo"
    res = ""
    for i in range(0, len(str1)):
        res += str1[i] + str2[i]
    return res
# str1 = input("Ingrese la primera palabra \n")
# str2 = input("Ingrese la segunda palabra \n")
# print(intercalar_strings(str1, str2))

# Lista al cubo
def elevar_al_cubo(lista):
    res = []
    for item in lista:
        res.append(item ** 3)
    return res

# casos de prueba
# print(elevar_al_cubo([1, 2, 3, 4, 5]))
# print(elevar_al_cubo([1, 242, 578, 757354873]))
# print(elevar_al_cubo([]))
# print(elevar_al_cubo([3]))


# Notas de clase
sample_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80,
		            "math": 90
            },
        }
    }
}

def calcular_notas(dict):
    nombre = dict["class"]["student"]["name"]
    nota_fisica = dict["class"]["student"]["marks"]["physics"]
    nota_historia = dict["class"]["student"]["marks"]["history"]
    nota_mate = dict["class"]["student"]["marks"]["math"]
    promedio = (nota_fisica + nota_historia + nota_mate)/3
    return {"name": nombre, "avg": promedio}
# print(calcular_notas(sample_dict))

# Eliminar los repetidos de una lista
test_list = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7]
test_list2 = ["pa", "pa", "pe", "pi"]
def eliminar_reps(list):
    res = []
    for item in list:
        if item not in res:
            res.append(item)
    return res
print(eliminar_reps(test_list2))
print(eliminar_reps([]))
print(eliminar_reps([3,3,3,3,3,3,3]))