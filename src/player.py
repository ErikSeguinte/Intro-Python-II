# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room, Item


class Player:
    def __init__(self, position: Room):
        self.position = position

        self.items = {}

    def move(self, direction: str):
        try:
            self.position = self.position.get_next(direction)
        except ValueError:
            raise ValueError
