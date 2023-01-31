a =input("primera palabra:")
b =input("segunta palabra:")

max_list = max(len(a), len (b)) #comprobar la cantidad de letrass

if (len(a)== len(b)):   #si tienenla mmisma cantidad
    print(" ".join([item for sublist in zip(a, b) for item in sublist if item != ""]))

if (len(a) != len(b)): #si no tienen la misma cantidad imprimir error
    print("error")