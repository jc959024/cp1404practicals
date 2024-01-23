"""(Incomplete) Tests for Song class."""
from song import Song

def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned

    # Test initial-value song
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)
    # TODO: Write tests to show this initialisation works
    assert initial_song.artist == "Powderfinger"
    assert initial_song.title == "My Happiness"
    assert initial_song.year == 1996
    assert initial_song.is_learned

    # TODO: Add more tests, as appropriate, for each method
    print("\nTest learn/unlearn song:")
    song = Song("Apple", "fruit band", 1999)
    print(f"Before learning: {song}")
    song.learn_song()
    assert song.is_learned
    print(f"After learning: {song}")
    song.unlearn_song()
    assert not song.is_learned
    print(f"After unlearning: {song}")


run_tests()
