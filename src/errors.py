class ItemDoesNotExistError(ValueError):
    pass

class ItemNotInInventory(ItemDoesNotExistError):
    pass


class CommandNotRecognizedError(TypeError):
    pass


class NoPathExists(ValueError):
    pass
