from vehicle import Vehicle

class Delorean(Vehicle):
    def __init__(self, color, maximum_occupancy, cargo_space, type_of_vehicle, Flux_Capacitor_Gigawatts):
        super().__init__(color, maximum_occupancy, cargo_space, type_of_vehicle)
        self.Flux_Capacitor_Gigawatts = Flux_Capacitor_Gigawatts
    
    def drive(self, sound):
        print(f"The {self.color} Delorean goes {sound}.")
    
    def stop(self):
        print(f"The Delorean stops in 1985.")

    def inMotion(self):
        self.drive("vroom"), self.stop()
        