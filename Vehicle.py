class Vehicle:
    """
    Base class for vehicles with a generic move action.
    """
    def __init__(self, model):
        self.model = model

    def move(self):
        """
        Generic move action - to be overridden by subclasses.
        """
        print(f"The {self.model} is moving.")

class Car(Vehicle):
    """
    Represents a car with a specific move action.
    """
    def move(self):
        print(f"The {self.model} is driving. 🚗")

class Plane(Vehicle):
    """
    Represents a plane with a specific move action.
    """
    def move(self):
        print(f"The {self.model} is flying. ✈️")

class Boat(Vehicle):
    """
    Represents a boat with a specific move action.
    """
    def move(self):
        print(f"The {self.model} is sailing. 🚢")

# Creating instances of different vehicle types
car = Car("Sedan")
plane = Plane("Boeing 747")
boat = Boat("Sailboat")

# Calling the move() method on each object
vehicles = [car, plane, boat]
for vehicle in vehicles:
    vehicle.move()