class Dog:
    # atributo de clase
    species = "Canis familiaris"

    def __init__(self, name, age):
        # atributos de instancia
        self.name = name
        self.age = age

    # métodos (comportamientos de mi clase)
    def speak(self, sound):
        print(f"{self.name} ladra diciendo: {sound}")

    def getold(self):
        self.age += 1


mia = Dog("Mia", 3)  # instancia de la clase Dog
pasi = Dog("Pasi", 5)  # otra instancia de la clase Dog

# print(type(mia))
# print(type(pasi))
# print(mia == pasi)
# print(mia.name)
# print(mia.age)
# print(mia.species)
# print(pasi.species)


class Dachshund(Dog):
    # def speak(self, sound="Arf"):
    #     print(f'{self.name} dice: {sound}')

    # ejemplo de overriding (sobreescribir)
    def speak(self, sound="arf"):
        return super().speak(sound)

    def getold(self):
        self.age += 3

    # ejemplo de extend
    def sleep(self):
        print("zzZZ")


capitan = Dachshund("Capitán", 9)
# print(capitan.age)
# capitan.getold()
# print(capitan.age)
# capitan.speak("Como puedo hablar si soy un perro?")
# mia.speak("Hola")
# capitan.speak()

# capitan.sleep()
# pasi.sleep()
