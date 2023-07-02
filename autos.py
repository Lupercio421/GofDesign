class Car:
    """A simple attempt to model a car"""
    def __init__(self, make, model, year):
        """Initialize car attributes"""
        self.make = make
        self.model = model
        self.year = year

        self.fuel_capacity = 25
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity"""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")

my_car = Car('Chevy', 'Cruze', 2014)

print(my_car.make)