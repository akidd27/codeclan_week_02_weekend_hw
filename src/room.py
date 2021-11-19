from src.bar_menu import bar_menu

class Room:
    
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.songs = []
        self.guests = []
        self.entry_fee = 5
        self.till = 0
        #Bar menu is dict in format "drink_name" : price
        self.drinks = bar_menu

    def add_song(self, song):
        self.songs.append(song)

    def can_check_in(self, guest):
        if len(self.guests) >= self.capacity:
            return False
        if guest.wallet < self.entry_fee:
            return False
        return True

    def check_in(self, guest):
        if self.can_check_in(guest):
            guest.wallet -= self.entry_fee
            self.till += self.entry_fee
            self.guests.append(guest)
            if guest.favourite_song in self.songs:
                return "Woo!"

    def check_out(self, guest):
        self.guests.remove(guest)

    def sell_drink(self, guest, drink):
        if drink in self.drinks:
            self.till += self.drinks[drink]
            guest.wallet -= self.drinks[drink]
        else:
            return f"We don't have {drink}"