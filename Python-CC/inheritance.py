class Car:
    """A simple ateempt to represent a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(selfself, mileage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("you can't roll back an odometer!")

    def incerment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initizlize attributes of the parent class"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', "model s", 2019)
print(my_tesla.get_descriptive_name())