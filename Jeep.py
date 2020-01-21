from vehicle import Vehicle

class Jeep(Vehicle):
    def __init__(self, color, maximum_occupancy, cargo_space, type_of_vehicle):
        super().__init__(color, maximum_occupancy, cargo_space, type_of_vehicle)
        