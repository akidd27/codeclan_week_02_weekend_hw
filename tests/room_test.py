import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room(1, 8)

        self.song1 = Song("Like a Prayer", "Madonna", "Like a Prayer")
        self.song2 = Song("Mamma Mia", "ABBA", "ABBA")

        self.guest1 = Guest("Sharon", 90, self.song1)
        self.guest2 = Guest("Linda", 20, self.song2)

    def test_room__has_number(self):
        self.assertEqual(1, self.room1.room_number)

    def test_room__has_capacity(self):
        self.assertEqual(8, self.room1.capacity)

    def test_room__can_add_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual(self.room1.songs[0], self.song1)

    def test_room__can_add_multiple_songs(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.assertEqual(2, len(self.room1.songs))

    def test_room__can_check_in_guest(self):
        self.room1.check_in(self.guest1)
        self.assertEqual(self.guest1, self.room1.guests[0])

    def test_room__can_check_out_guest(self):
        self.room1.check_in(self.guest1)
        self.room1.check_out(self.guest1)
        self.assertEqual(0, len(self.room1.guests))

    def test_room__does_not_exceed_capacity(self):
        #create room with capacity of 2
        self.room2 = Room(2, 2)
        #create 3rd guest
        self.guest3 = Guest("Abigail", 50, self.song2)
        #add 3 guests
        self.room2.check_in(self.guest1)
        self.room2.check_in(self.guest2)
        self.room2.check_in(self.guest3)
        #assert that the room has only 2 guests 
        self.assertEqual(2, len(self.room2.guests))
        #assert that guest 3 is not in the room
        self.assertNotIn(self.guest3, self.room2.guests)

    def test_room__does_not_check_in_without_fee(self):
        #create guest with insufficient funds
        self.guest4 = Guest("Laura", 0, self.song2)
        #attempt to check in to room1 (entry fee of 5)
        self.room1.check_in(self.guest4)
        self.assertEqual(0, len(self.room1.guests))

    def test_room__check_in_pays_entry_fee(self):
        self.room1.check_in(self.guest1)
        self.assertEqual(85, self.guest1.wallet)
        self.assertEqual(5, self.room1.till)

    def test_room__guest_woos_if_favourite_song_in_songs(self):
        self.room1.add_song(self.song1)
        self.assertEqual("Woo!", self.room1.check_in(self.guest1))

    def test_sell_drink(self):
        self.room1.check_in(self.guest1)
        self.room1.sell_drink(self.guest1, "beer")
        self.assertEqual(9, self.room1.till)
        self.assertEqual(81, self.guest1.wallet)

    def test_sell_drink__only_sells_if_drink_on_menu(self):
        self.room1.check_in(self.guest1)
        self.room1.sell_drink(self.guest1, "champagne")
        self.assertEqual(5, self.room1.till)
        self.assertEqual(85, self.guest1.wallet)
        self.assertEqual("We don't have champagne", self.room1.sell_drink(self.guest1, "champagne"))