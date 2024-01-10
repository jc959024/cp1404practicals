from unreliable_car import UnreliableCar

# Create an UnreliableCar
my_unreliable_car = UnreliableCar("Car 1", 50, 70)

# Drive 30 km with a chance based on reliability
distance_driven = my_unreliable_car.drive(30)

# Display details and distance driven
print("Details after driving:")
print(my_unreliable_car)
print(f"Distance Driven: {distance_driven} km")

