# ANITALAVALATINA
string = input('Escriba una oración: ')
input_min = string.lower()
input_min = input_min.replace(" ", "")
if input_min != input_min[::-1]:
    print('Esta frase NO es un palíndromo')
else: 
    print('La frase SÍ es un palíndromo')

# i = 0
# is_palindromo = True
# while i < len(input_min) / 2 and is_palindromo:
#     if input_min[i] != input_min[(i+1)*-1]:
#         print('Esta frase NO es un palíndromo')
#         is_palindromo = False
#     else:
#         i += 1

# if is_palindromo: print('La frase SÍ es un palíndromo')

