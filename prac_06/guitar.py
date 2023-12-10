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

# Example usage
if __name__ == "__main__":
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(my_guitar)
    print(f"Age: {my_guitar.get_age()} years")
    print(f"Is Vintage: {my_guitar.is_vintage()}")
