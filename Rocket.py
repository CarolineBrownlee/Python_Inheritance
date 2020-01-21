from vehicle import Vehicle

class Rocket(Vehicle):
    def __init__(self, color, maximum_occupancy, cargo_space, type_of_vehicle):
        super().__init__(color, maximum_occupancy, cargo_space, type_of_vehicle)
        self.has_launcher = True

    def drive(self):
        print(f"The {self.color} rocket sounds like thunder and smells like fire!")