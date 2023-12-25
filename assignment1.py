"""
Name:HuayuZhong
Date started:24/12
GitHub URL:https://github.com/jc959024/cp1404practicals
"""

import csv

SONG_FILE = "songs.csv"
MENU = """Menu:
L - List songs
A - Add new song
C - Complete a song
Q - Quit"""

# Main function
def main():
    print("Songs To Learn 1.0 - by [HuayuZhong]")
    songs = load_songs()
    print(f"{len(songs)} songs loaded")

    choice = input(MENU + "\n>>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            list_songs(songs)
        elif choice == 'A':
            add_song(songs)
        elif choice == 'C':
            complete_song(songs)
        else:
            print("Invalid choice")
        choice = input(MENU + "\n>>> ")

    save_songs(songs)
    print(f"{len(songs)} songs saved to {SONG_FILE}")
    print("Have a nice day :)")


def load_songs():
    songs = []
    try:
        with open(SONG_FILE, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                songs.append(row)
    except FileNotFoundError:
        print("No existing song file found. A new one will be created.")
    return songs

# Function to list songs
def list_songs(songs):
    print("List of songs:")
    for i, song in enumerate(songs, 1):
        status = 'learned' if song['learned'] == 'Yes' else 'unlearned'
        print(f"{i}. {song['title']} by {song['artist']} ({song['year']}) - {status}")

# Function to add a new song
def add_song(songs):
    title = input("Title of the new song: ")
    artist = input("Artist: ")
    year = input("Year: ")
    songs.append({'title': title, 'artist': artist, 'year': year, 'learned': 'No'})
    print("New song added!")

# Function to mark a song as learned
def complete_song(songs):
    list_songs(songs)
    song_number = int(input("Enter the number of the song to mark as learned: "))
    if 0 < song_number <= len(songs):
        songs[song_number - 1]['learned'] = 'Yes'
        print(f"{songs[song_number - 1]['title']} marked as learned.")
    else:
        print("Invalid song number.")

# Function to save songs to the file
def save_songs(songs):
    with open(SONG_FILE, 'w', newline='') as file:
        fieldnames = ['title', 'artist', 'year', 'learned']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for song in songs:
            writer.writerow(song)

# Run the program
if __name__ == '__main__':
    main()
