class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = 2022  # Assuming the current year is 2022
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        """Compare Guitars by their year."""
        return self.year < other.year

    def main():
        guitars = []

        with open('guitars.csv', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name, year, cost = parts
                    guitars.append(Guitar(name, int(year), float(cost)))

        print("These are my guitars:")
        for guitar in guitars:
            print(guitar)

        guitars.sort()

        print("\nGuitars sorted by year:")
        for guitar in guitars:
            print(guitar)

    if __name__ == "__main__":
        main()

if __name__ == "__main__":
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(my_guitar)
    print(f"Age: {my_guitar.get_age()} years")
    print(f"Is Vintage: {my_guitar.is_vintage()}")