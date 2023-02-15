"""Programa que soluciona el problema Fizz Buzz"""

# El programa recibe un número del usuario e imprime en pantalla
# todos los números del 1 al número ingresado.
# Sin embargo, si el número el múltiplo de 3 imprime "Fizz" y si
# el número es múltiplo de 5 imprime "Buzz". Si el número es
# múltiplo tanto de 3 como de 5, imprime "FizzBuzz"

num = input('Ingrese un numero entero mayor a 0 \n')
x = 0

for x in range(1, int(num)+1):
    if x % 3 == 0 and x % 5 == 0:
      print('FizzBuzz') 
    elif x % 3 == 0:
      print('Fizz')
    elif x % 5 == 0:
      print('Buzz')
    else:
       print(x)


