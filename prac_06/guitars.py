from guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    # Get guitar details from user
    # Uncomment these lines for user input
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitar = Guitar(name, year, cost)
    #     guitars.append(guitar)
    #     print(f"{guitar} added.\n")
    #     name = input("Name: ")

    # Hardcoded data for testing
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    # Displaying guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()
