"""..."""

from song import Song
from songcollection import SongCollection
my_song_collection = SongCollection()
#Song


import csv

#Song
class Song:
    def __init__(self, title, artist, year, is_learned=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def __str__(self):
        learned_marker = "*" if self.is_learned else ""
        return f"{learned_marker} {self.title} - {self.artist} ({self.year})"

#SongList
class SongList:
    def __init__(self, filename):
        self.filename = filename
        self.songs = []
        self.load_songs()

    def load_songs(self):
        with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                title, artist, year, is_learned = row
                self.songs.append(Song(title, artist, int(year), is_learned == 'True'))

    def save_songs(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for song in self.songs:
                writer.writerow([song.title, song.artist, song.year, song.is_learned])

    def add_song(self, title, artist, year):
        self.songs.append(Song(title, artist, year))

    def complete_song(self, song_number):
        if 0 < song_number <= len(self.songs):
            song = self.songs[song_number - 1]
            if not song.is_learned:
                song.is_learned = True

                return f"{song.title} by {song.artist} learned"
            else:
                return f"You have already learned {song.title}"
        else:
            return "Invalid song number"

    def display_songs(self):
        self.songs.sort(key=lambda x: (x.year, x.title))
        for i, song in enumerate(self.songs, start=1):

            print(f"{i}. {song}")
        learned_count = sum(song.is_learned for song in self.songs)
        print(f"{learned_count} songs learned, {len(self.songs) - learned_count} songs still to learn.")

def main():
    song_list = SongList('songs.csv')
    print("Song List 1.0 - by Zhicheng Liang")
    print(f"{len(song_list.songs)} songs loaded.")
    while True:
        print("Menu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>> ").upper()#notice
        if choice == 'D':
            song_list.display_songs()
        elif choice == 'A':
            title = input("Title: ").strip()
            while not title:
                print("Input can not be blank.")#11111
                title = input("Title: ").strip()
            artist = input("Artist: ").strip()
            while not artist:
                print("Input can not be blank.")
                artist = input("Artist: ").strip()
            year = input("Year: ").strip()
            while not year.isdigit() or int(year) <= 0:
                print("Invalid input; enter a valid number.")
                year = input("Year: ").strip()
            song_list.add_song(title, artist, int(year))
            print(f"{title} by {artist} ({year}) added to song list.")
        elif choice == 'C':
            song_number = input("Enter the number of a song to mark as learned.\n>>> ").strip()
            while not song_number.isdigit() or int(song_number) <= 0:
                print("Number must be > 0.")
                song_number = input(">>> ").strip()
            print(song_list.complete_song(int(song_number)))
        elif choice == 'Q':
            song_list.save_songs()
            print(f"{len(song_list.songs)} songs saved to songs.csv\nMake some music!")
            break
        else:
            print("Invalid menu choice")

if __name__ == "__main__":

    main()