import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Toxic", "Britney Spears", "In the Zone")

    def test_song__has_name(self):
        self.assertEqual("Toxic", self.song.name)

    def test_song__has_artist(self):
        self.assertEqual("Britney Spears", self.song.artist)

    def test_song__has_album(self):
        self.assertEqual("In the Zone", self.song.album)
