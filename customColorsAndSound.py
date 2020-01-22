# INHERITANCE:
# 1. Allows one type to include all of the public properties and methods of another type.
# 2. It reduces duplicated code when many types in a program all have the same properties and methods.

# 1. FINISHED Define 5 of your favorite vehicles
# 2. FINISHED Move all common properties in your vehicles to a new Vehicle class.
# 3. FINISHED Create an instance of each vehicle.
from vehicle import Vehicle
from Jeep import Jeep
from LandRover import LandRover
from Rocket import Rocket
from Delorean import Delorean
from StationWagon import StationWagon

Janes_Car = Jeep("black", 4, "13 ft3", "SUV")
Annies_Car = LandRover("maroon", 7, "27.5 ft3", "SUV" )
Josephs_Car = Rocket("white", 1, "none", "Spaceship")
Mollys_Car = Delorean("grey", 2, "none", "Time Machine", 1.21)
Moms_Car = StationWagon("purple", 6, "34 ft3", "SUV")

# 4. FINISHED Define a different value for each vehicle's properties.

# 5. FINISHED Create a drive() method in the Vehicle class.

# 6. FINISHED Override the drive() method in all the other vehicle classes.
 
# Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# Janes_Car.drive()
# Moms_Car.drive("putter")
# Josephs_Car.drive()
Mollys_Car.drive("swooooosh")
# Annies_Car.drive()

# 7. FINISHED Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.

Mollys_Car.turn("south")

# 8. FINISHED Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."

Josephs_Car.stop()
Mollys_Car.stop()
Annies_Car.stop()


# 9. FINISHED Make your vehicle instances perform all three behaviors.

Mollys_Car.inMotion()



