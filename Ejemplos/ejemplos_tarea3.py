# Uso de ciclo WHILE cuando la cantidad de ciclos está indeterminada
continuar = True
while continuar:
    num = int(input("Ingrese un numero mayor a 0. Ingrese -1 para salir \n"))
    if num == -1:
      continuar = False
    print("El numero es: " + str(num))
