import os
import arit

a = 1
b = 2

arit.imprimir_numeros(a, b)
res = arit.sumar_numeros(a, 10)
print(res)
print(arit.API_URL)


file = open("demofile.txt", "a")
file.write("Texto de prueba")
file.close()

file = open("demofile.txt", "w")
file.write("Write sobreescribe \n")
file.write("Write sobreescribe \n")
file.write("Write sobreescribe \n")
file.write("Write sobreescribe \n")
file.write("Write sobreescribe \n")
file.close()

file = open("demofile.txt")
# print(file.read())

for line in file:
  print(line)

file.close()
# file2 = open("demofile2.txt", "a")

# file2.write("Hola archivo \n")

if (os.path.exists("demofile.txt")) == False:
  file3 = open("demofile.txt", "x")
else: 
  file3 = open("demofile.txt")

# file.close()
# file2.close()
