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

## Testing 
h = Elevator(1, 10)
h.go_to_floor(10)
h.go_to_floor(1)