from taxi import Taxi

from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").lower()

        if user_choice == 'q':
            break
        elif user_choice == 'c':
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ")

            if taxi_choice.isdigit():
                taxi_choice = int(taxi_choice)
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                    print(f"Bill to date: ${total_bill:.2f}")
                else:
                    print("Invalid taxi choice")
            else:
                print("Invalid input")

        elif user_choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${total_bill:.2f}")
                continue

            distance_input = input("Drive how far? ")
            if distance_input.replace('.', '', 1).isdigit():
                distance = float(distance_input)
                cost = current_taxi.drive(distance)
                total_bill += cost
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                print(f"Bill to date: ${total_bill:.2f}")
            else:
                print("Invalid input")

if __name__ == '__main__':
    main()
