# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
import errors

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.w_to = None
        self.s_to = None
        self.e_to = None

        self.items = {}

        self.connections = None

    def get_next(self, direction: str):
        if not self.connections:
            self.connections = {
                "n": self.n_to,
                "e": self.e_to,
                "s": self.s_to,
                "w": self.w_to,
            }

        if not self.connections[direction]:
            raise errors.NoPathExists(direction)
        return self.connections[direction]

    def enter(self):
        print(f"{self.name}\n{self.description}")
        for k, v in self.items.items():
            print(f"**There is a {v.name} here")
