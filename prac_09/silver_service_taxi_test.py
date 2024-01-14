from silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi
my_silver_taxi = SilverServiceTaxi("Hummer", 200, 4)

# Drive 18 km
my_silver_taxi.drive(18)

# Display details and total fare
print("Details after driving:")
print(my_silver_taxi)
print(f"Total Fare: ${my_silver_taxi.get_fare():.2f}")
