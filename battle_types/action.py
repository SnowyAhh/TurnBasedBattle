from enum import Enum

class ActionTypes(Enum):
    HEALTH = 1, # Heals self
    ATTACK = 2, # Attacks opponent

class Action:
    def __init__(self, name, type, points, description) -> None:
        self.name = name
        self.type = type
        self.points = points
        # For attack, points = base attack for move
        # For health, points = percentage of health healed
        self.description = description