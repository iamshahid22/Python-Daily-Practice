class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self): # This is an instance method
        return f"{self.name} is {self.age} years old"
