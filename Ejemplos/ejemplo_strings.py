string_ex = "Esto es una string"

# Acceder a caracteres individuales
print("El primer caracter es {0} y el último {1}".format(
  string_ex[0], string_ex[-1]
))

# Checkear si otra string está incluida en la primera
sub_string = "string"
print("Es {0} que la string contiene la palabra {1}".format(
  sub_string in string_ex, sub_string
))

# Algunos métodos útiles
# MAYÚSCULAS
print (string_ex.upper())

# minúsculas
print (string_ex.lower())

# Reemplazar una string por otra
print(string_ex.replace("string", "prueba"))