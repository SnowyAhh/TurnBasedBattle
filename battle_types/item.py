from enum import Enum

class ItemTypes(Enum):
    HEALTH = 1,
    ATTACK = 2

class Item:
    def __init__(self, name, type, points, description) -> None:
        self.name = name
        self.type = type
        self.points = points # How much it buffs
        self.description = description
        