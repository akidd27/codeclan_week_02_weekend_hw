import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Heart of Glass", "Blondie", "Parallel Lines")
        self.guest = Guest("Roger", 45, self.song)
    
    def test_guest__has_name(self):
        self.assertEqual("Roger", self.guest.name)

    def test_guest__has_wallet(self):
        self.assertEqual(45, self.guest.wallet)

    def test_guest__can_woo(self):
        self.assertEqual("Woo!", self.guest.woo())
    
    def test_guest__has_favourite_song(self):
        self.assertEqual(self.song, self.guest.favourite_song)