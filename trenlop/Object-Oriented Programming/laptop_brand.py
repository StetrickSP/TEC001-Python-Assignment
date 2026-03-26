class Laptop:
    def __init__(self, brand: str, ram: int):
        self.brand = brand
        self.ram = ram
        self.is_on = True

    def get_ram(self):
        return self.ram
    
    def power_button(self):
        if self.is_on: 
            print(f"The laptop is_on status: {self.is_on}")
            self.is_on = False 
            print(f"The {self.brand} is now shutting down...")
        elif self.is_on == False: 
            print(f"The laptop is_on status: {self.is_on}")
            self.is_on = True
            print(f"The {self.brand} is now starting...")
    
lap1 = Laptop("Gucci", "16GB")
lap1.power_button()
print(dir(lap1))
