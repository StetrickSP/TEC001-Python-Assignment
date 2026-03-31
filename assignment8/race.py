import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.current_speed += speed_change

            if car.current_speed < 0:
                car.current_speed = 0
            if car.current_speed > car.max_speed:
                car.current_speed = car.max_speed

            car.drive(1)

    def print_status(self):
        print("\n--- Race Status ---")
        print(f"{'Car':<10}{'Speed':<10}{'Distance':<10}")

        for car in self.cars:
            print(f"{car.registration_number:<10}{car.current_speed:<10}{car.travelled_distance:<10}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.kilometers:
                return True
        return False
    

## Testing
print("\n=== Race Simulation ===")

cars = []
for i in range(10):
    reg = "ABC-" + str(i+1)
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    hours += 1
    race.hour_passes()

    if hours % 10 == 0:
        race.print_status()

race.print_status()
print(f"\nRace finished in {hours} hours!")