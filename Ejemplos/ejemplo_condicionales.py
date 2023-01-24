a = 142
b = 5000
c = 666

if a == b:
  print("A es igual a B")
elif a < b:
  print("A es menor que B")
elif a <= b:
  print("A es menor o igual que B")
elif a > b:
  print("A es mayor que B")
elif a >= b:
  print("A es mayor o igual que B")
else:
  print("Caí en la opción por defecto")

if b > a and b < c:
  print("B está entre A y C")
elif a > b or a > c:
  print("A es mayor a B o C (o a ambas)")
else:
  print("Caí en la opción por defecto")