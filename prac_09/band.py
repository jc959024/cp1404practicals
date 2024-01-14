class Band:
    """Band class for storing details of a band."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return a string showing each musician playing their first (or no) instrument."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)
