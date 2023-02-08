# Factorial de un numero num
def factorial(num):
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
# print(factorial(num))

# triangulo de N niveles
def triangulo(n):
    if n <= 0:
        return "El numero debe ser mayor a 0"
    triangulo = ""
    for i in range(1, n+1):
        triangulo += str(i) + " "
        print(triangulo)
# n = int(input("Ingrese un numero mayor 0: \n"))
# triangulo(n)

# strings intercaladas
def strings_intercaladas(str1, str2):
    if len(str1) != len(str2):
        return "Las strings deben ser del mismo largo"
    res = ""
    for i in range(0, len(str1) ):
        res += str1[i] + str2[i]
    return res
# str1 = input("Ingrese la primera palabra \n")
# str2 = input("Ingrese la segunda palabra \n")
# print(strings_intercaladas(str1, str2))

# Lista al cubo
def lista_al_cubo():
    lista = [1, 2, 3, 4, 5]
    res = []
    for i in lista:
        res.append(i ** 3)
    return res
# print(lista_al_cubo())

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

def notas_de_clase(dict):
    nombre = dict["class"]["student"]["name"]
    fisica = dict["class"]["student"]["marks"]["physics"]
    historia = dict["class"]["student"]["marks"]["history"]
    mate = dict["class"]["student"]["marks"]["math"]
    promedio = (fisica + historia + mate)/3
    return {"name": nombre, "avg": promedio}
# print(notas_de_clase(sample_dict))

# Eliminar los repetidos de una lista
test_list = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7]
def eliminar_reps(list):
    res = []
    for item in list:
        if item not in res:
            res.append(item)
    return res
# print(eliminar_reps(test_list))