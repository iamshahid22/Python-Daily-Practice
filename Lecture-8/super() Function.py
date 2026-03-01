class Car:
    def __init__(self, brand):
        self.brand = brand

class Toyota(Car):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

t = Toyota("Toyota", "Fortuner")
print(t.brand, t.model)