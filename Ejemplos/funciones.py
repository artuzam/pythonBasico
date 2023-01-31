import modulo_arit as ma

print(ma.suma(2, 2))
print(ma.resta(4, 2))
print(ma.API_URL)

print(dir(ma))


file = open("demofile.txt")

# for line in file:
#   print(line)

# file2 = open("demofile2.txt", "a")

# file2.write("Hola archivo \n")

# if (os.path.exists("demofile.txt")) == False:
#   file3 = open("demofile.txt", "x")

file.close()
# file2.close()
