## Elevator
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator moving up: Floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator moving down: Floor {self.current_floor}")

    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()


## Building 
class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom = bottom_floor
        self.top = top_floor
        self.elevators = []

        for i in range(elevator_count):
            print("Elevator created:", i)
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning elevator {elevator_number}")
            self.elevators[elevator_number].go_to_floor(destination_floor)

## Testing
b1 = Building(1, 10, 2)
b1.run_elevator(0, 3)
b1.run_elevator(1, 4)
