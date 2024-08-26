class Vehicle:
    def __init__(self, make = "") -> None:
        self.make = make
    def description(self):
        print(f'hang san xuat: {self.make}')

class Car(Vehicle):
    def __init__(self, make="", model = "") -> None:
        super().__init__(make)
        self.model = model
    def description(self):
        super().description()
        print(f'Ten dong xe: {self.model}')

class ElectricCar(Car):
    def __init__(self, make="", model="", battery_size = "") -> None:
        super().__init__(make, model)
        self.battery_size = battery_size
    def description(self):
        super().description()
        print(f'Battery size: {self.battery_size}')
    
vehicle = Vehicle('Tesla')
vehicle.description()
car = Car('Tesla', 'model X')
car.description()
cyberTruck = ElectricCar('Tesla', 'v1', '5000mAh')
cyberTruck.description()