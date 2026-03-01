class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")


class ToyotaCar(Car):   # Inheriting from Car
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):   # Inheriting from ToyotaCar
    def __init__(self, type, brand):
        super().__init__(brand)
        self.type = type


car1 = Fortuner("diesel", "Toyota")
car1.start()