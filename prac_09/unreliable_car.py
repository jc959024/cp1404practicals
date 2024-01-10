import random
from car import Car

class UnreliableCar(Car):
    """A derived class for an UnreliableCar that inherits from Car."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance, based on the parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive only if a random number is less than reliability."""
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0
