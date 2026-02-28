class Person:
    # Parameterized Constructor
    def __init__(self, name, age):
        self.name = name  # Initialize the instance attribute 'name'
        self.age = age    # Initialize the instance attribute 'age'
        print(f"A new person named {self.name} has been created.")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects (instances) of the Person class
person1 = Person("Alice", 25) # The constructor is called automatically here
person2 = Person("Bob", 30)

# Accessing methods and attributes
person1.display()
person2.display()
