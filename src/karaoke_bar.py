class KaraokeBar:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def closing_time(self):
        for room in self.rooms:
            self.till += room.till
            room.till = 0
            room.guests.clear()