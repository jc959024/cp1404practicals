from prac_06.car import Car

def main():
    # Original my_car code with added name
    my_car = Car(180, "My Car")
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    # New code for limo with name
    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print(f"{limo.name} has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)

main()
