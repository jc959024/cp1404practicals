"""..."""


class Song:
    """..."""

    def __init__(self, title="", artist="", year=0, is_learned=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def __str__(self):
        learned_status = " (learned)" if self.is_learned else ""
        return f"{self.title} by {self.artist}, released in {self.year}{learned_status}"

    def learn_song(self):
        self.is_learned = True

    def unlearn_song(self):
        self.is_learned = False
