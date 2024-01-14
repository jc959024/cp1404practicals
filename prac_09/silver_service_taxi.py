from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A specialized version of a Taxi that includes additional charges for fanciness and flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the total fare including additional charges."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string with additional information about the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
