import uuid


class Employee:
    # estos se llaman atributos de clase, se inicializan
    # automáticamente
    id = str(uuid.uuid4())

    # todas las clases deben tener un método __init__ que
    # inicializa sus atributos
    def __init__(self, name, position, tenure):
        # estos se llaman atributos de instacia
        self.name = name
        self.position = position
        self.tenure = tenure

    def __str__(self):
        tenure_in_years = self.tenure / 12
        return f"ID: {self.id} \nName: {self.name} \nPosition: {self.position} \nTenure: {tenure_in_years} years"

    def get_employee_info(self):
        tenure_in_years = self.tenure / 12
        return f"ID: {self.id} \nName: {self.name} \nPosition: {self.position} \nTenure: {tenure_in_years} years"

    def speak(self, sound):
        print(f"{self.name} dice: {sound}")


pedro = Employee("Pedro", "Software Engineer", 6)
maria = Employee("Maria", "QA Engineer", 24)
# print(pedro)
# print(pedro.get_employee_info())
# print(maria.get_employee_info())
# pedro.speak("Hola")


class Manager(Employee):
    def __init__(self, name, position, tenure, juniors=[]):
        super().__init__(name, position, tenure)
        self.juniors = juniors

    # def get_employee_info(self):
    #     self.name = 'Mr. ' + self.name
    #     return f"ID: {self.id} \nName: {self.name} \nPosition: {self.position} \nTenure: {self.tenure} months"

    def get_employee_info(self):
        self.name = "Mr./Mrs. " + self.name
        return super().get_employee_info()

    def list_juniors(self):
        if len(self.juniors) == 0:
            print(f"{self.name} has no juniors")
        else:
            for employee in self.juniors:
                print(employee.name)


marco = Manager("Marco", "Project Manager", 50, [pedro, maria])
luisa = Manager("Luisa", "QA Manager", 120)
# print(luisa.get_employee_info())
# print(type(marco))
# print(type(pedro))
# print(isinstance(marco, Employee))
# print(isinstance(marco, Manager))
# print(isinstance(luisa, Employee))
# print(isinstance(maria, Manager))
print(marco.get_employee_info())
marco.list_juniors()
# luisa.list_juniors()
# print(luisa.name)
