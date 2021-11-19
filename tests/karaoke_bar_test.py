import unittest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        self.karaoke_bar = KaraokeBar("Caraoke", 1000)
        self.room1 = Room(3, 10)
        self.karaoke_bar.add_room(self.room1)
        self.song1 = Song("Bad Moon Rising", "Creedence ClearWater Revival", "Green River")
        self.guest1 = Guest("Adam", 50, self.song1)

    def test_has_name(self):
        self.assertEqual("Caraoke", self.karaoke_bar.name)

    def test_can_add_room(self):
        self.karaoke_bar
        self.assertEqual(self.room1, self.karaoke_bar.rooms[0])

    def test_closing_time__clears_rooms(self):
        self.karaoke_bar.closing_time()
        for room in self.karaoke_bar.rooms:
            self.assertEqual(0, len(room.guests))

    def test_closing_time__collects_money_from_room_tills(self):
        self.karaoke_bar.rooms[0].check_in(self.guest1)
        self.karaoke_bar.closing_time()
        self.assertEqual(1005, self.karaoke_bar.till)
        self.assertEqual(0, self.karaoke_bar.rooms[0].till)
