from enum import Enum

class ActionTypes(Enum):
    ATTACK = 1

class Action:
    def __init__(self, name, type, points, description) -> None:
        self.name = name
        self.type = type
        self.points = points
        self.description = description