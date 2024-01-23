"""(Incomplete) Tests for SongCollection class."""
from song import Song
from songcollection import SongCollection

def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert not song_collection.songs  # an empty list is considered False

    # Test loading songs
    print("Test loading songs:")
    song_collection.load_songs('songs.json')
    print(song_collection)
    assert song_collection.songs  # assuming file is non-empty, non-empty list is considered True

    # Test adding a new Song with values
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)

    # Test sorting songs
    print("Test sorting - year:")
    song_collection.sort("year")
    print(song_collection)

    song_collection.save_songs('songs.json')

    # Test learned and unlearned songs
    print("Test learned/unlearned count:")
    print("Unlearned songs:", song_collection.get_number_of_unlearned_songs())
    print("Learned songs:", song_collection.get_number_of_learned_songs())


run_tests()
