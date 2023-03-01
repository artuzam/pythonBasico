# ejemplos funciones como parámetros o como valor de retorno
# función como parámetro
def inner():
    print("Soy la funcion inner")


def outer(function):
    function()


# outer(inner)

# ejemplo de función como parámetro con sorted()
animales = ['perro', 'gato', 'paloma']
# print(sorted(animales))
# print(sorted(animales, key=len))


def reverse_len(s):
    return -len(s)


# print(sorted(animales, key=reverse_len))

# ejemplo de función como valor de retorno


def outer():
    def inner():
        print("I am function inner")
    return inner


function = outer()
# function()
# outer()()

# ejemplos de lambda
# funcionamiento de función normal (def) y lambda


def reverse(s):
    return s[::-1]

# print(reverse('Hola'))


def reverselambda(s): return s[::-1]
# print(reverselambda('Hola'))

#  otro ejemplo de lambda
# print((lambda a, b, c: (a+b+c)/3)(1,2,3))


# ejemplo de lambda con sorted()
animales = ['perro', 'gato', 'paloma']
# print(sorted(animales, key=lambda s: -len(s)))


# ejemplos de map()
# reverse a todas las strings de una lista con map()
animales = ['perro', 'gato', 'paloma']
iterator = map(reverse, animales)
# for i in iterator:
#     print(i)
# print(list(iterator))

# reverse a las strings con lambda
# print(list(map(lambda s: s[::-1], animales)))

# map con múltiples iterables
# print(list(map(lambda a, b, c: a+b+c,
#   [1, 2, 3], [10, 20, 30], [100, 200, 300])))

# ejemplos de filter
# filter con función normal (def)
numberlist = [1, 111, 2, 222, 3, 333]


def mayorque_100(x):
    return x > 100


# print(list(filter(mayorque_100, numberlist)))

# filter con lambda
# print(list(filter(lambda x: x > 100, numberlist)))

# ejemplo de filter con funciones nativas y def
animales = ['perro', 'PERRO', 'gato', 'GATO', 'paloma', 'PALOMA']


def all_caps(s):
    return s.isupper()


# print(list(filter(all_caps, animales)))

# ejemplo de filter con funciones nativas y lambda
# print(list(filter(lambda s: s.isupper(), animales)))
