class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

dog1 = Dog("Buddy", 3)
dog2 = Dog("Milo", 5)

print(dog1.name) # Output: Buddy
print(dog2.name) # Output: Milo
