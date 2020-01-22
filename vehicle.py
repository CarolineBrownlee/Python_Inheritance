class Vehicle:
    def __init__(self, color, maximum_occupancy, cargo_space, type_of_vehicle):
        self.color = color
        self.maximum_occupancy = maximum_occupancy
        self.cargo_space = cargo_space
        self.type_of_vehicle = type_of_vehicle

    def drive(self):
        print("Vrooom!")
    
    def stop(self):
        print(f"The vehicle has arrived at its destination.")

    def turn(self, direction):
        print(f"You turn {direction}.")