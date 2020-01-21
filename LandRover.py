from vehicle import Vehicle

class LandRover(Vehicle):
    def __init__(self, color, maximum_occupancy, cargo_space, type_of_vehicle):
        super().__init__(color, maximum_occupancy, cargo_space, type_of_vehicle)
        self.luxury_vehicle = True

    def drive(self):
        print(f"The {self.color} Land Rover sounds like the crackling fire of burning $100 bills.")