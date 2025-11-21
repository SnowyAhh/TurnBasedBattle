from enum import Enum

class ItemTypes(Enum):
    HEALTH = 1,
    ATTACK = 2,
    CRIT_RATE = 3,
    CRIT_DAMAGE = 4,
    SPEED = 5

class Item:
    def __init__(self, name: str, type: ItemTypes, points: float | int, 
                 description: str) -> None:
        self.name = name
        self.type = type
        self.points = points # How much it buffs
        self.description = description
        