class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.odometer = 0

    def drive(self, miles):
        self.odometer += miles
        print(f"The {self.brand} {self.model} has driven {miles} miles.")
    
car1 = Car("Toyota", "Camry")
car1.drive(18)
car1.drive(20)
print(f"This {car1.brand} {car1.model} has driven {car1.odometer} miles in total.")
        