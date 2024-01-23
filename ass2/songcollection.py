import json
from song import Song

class SongCollection:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_number_of_unlearned_songs(self):
        return sum(1 for song in self.songs if not song.is_learned)

    def get_number_of_learned_songs(self):
        return sum(1 for song in self.songs if song.is_learned)

    def load_songs(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.songs = [Song(**song_data) for song_data in data]

    def save_songs(self, filename):
        with open(filename, 'w') as file:
            json.dump([song.__dict__ for song in self.songs], file, indent=4)

    def sort(self, sort_key):
        self.songs.sort(key=lambda song: (getattr(song, sort_key), song.title))




