class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show(self):
        print(self.name, self.language, self.get_salary())

d = Developer("Shahid", 60000, "Python")
d.show()