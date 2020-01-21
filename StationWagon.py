from vehicle import Vehicle

class StationWagon(Vehicle):
    def __init__(self, color, maximum_occupancy, cargo_space, type_of_vehicle):
        super().__init__(color, maximum_occupancy, cargo_space, type_of_vehicle)
        self.has_wood_panel_sidewalls = True

    def drive(self, sound):
        print(f"The {self.color} station wagon goes {sound}!")

        