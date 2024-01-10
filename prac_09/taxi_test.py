from taxi import Taxi

# Create a new taxi
my_taxi = Taxi("Prius 1", 100, 1.23)

# Drive 40 km
my_taxi.drive(40)

# Display details and current fare
print("Details after driving 40 km:")
print(my_taxi)

# Start a new fare
my_taxi.start_fare()

# Drive 100 km
my_taxi.drive(100)

# Display details and current fare
print("\nDetails after driving 100 km:")
print(my_taxi)
print(f"Current Fare: ${my_taxi.get_fare():.2f}")
