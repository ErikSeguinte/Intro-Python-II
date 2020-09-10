from player import Player, Room, Item
import errors
from time import sleep

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

room["foyer"].items["sword"] = Item("sword")


def get(player: Player):
    def get_item(item: str):
        room = player.position
        if item in room.items.keys():
            new_item = room.items.pop(item)
            player.items[item] = new_item
            print("got item")
        else:
            raise errors.ItemDoesNotExistError(item)

    return get_item


def drop(player: Player):
    def drop_item(item: str):
        room = player.position
        if item in player.items.keys():
            new_item = player.items.pop(item)
            room.items[item] = new_item
            print("dropped item")
        else:
            raise errors.ItemNotInInventory(item)

    return drop_item

def print_output_response(s:str):
    print(s)
    sleep(1)
    print("\n" *2)



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room["outside"])
get_item = get(player)
drop_item = drop(player)

# Write a loop that:


valid_input = set("neswqi")
valid_input.update({"get", "drop"})

while True:
    player.position.enter()
    command = input("\nWhere would you like to go?\n").strip().lower().split(" ")
    command.append(" ")
    try:
        if command[0] not in valid_input:
            raise errors.CommandNotRecognizedError(command[0])
        if command[0] == "q":
            print("Thank you for playing")
            break
        elif command[0] == "i":
            item: Item
            print("Inventory")
            print("=========")
            for k, item in player.items.items():
                print(item.name)

            print()
            print("=========")
        else:
            if command[0] == "get":
                get_item(command[1])
            elif command[0] == "drop":
                drop_item(command[1])
            else:
                player.move(command[0])

    except errors.CommandNotRecognizedError:
        print_output_response("I do not understand that command")
        continue

    except errors.NoPathExists:
        print_output_response("You cannot go that way")
        continue

    except errors.ItemNotInInventory:
        print_output_response("You do not have that item")
        continue
    except errors.ItemDoesNotExistError:
        print_output_response("That does not exist here")
        continue


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
