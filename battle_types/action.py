from enum import Enum

class ActionTypes(Enum):
    HEALTH = 1, # Heals self
    ATTACK = 2, # Attacks opponent
    RECOVER = 3 # Recover stamina and mana

class ActionCategories(Enum):
    PHYSICAL = 1,
    MAGICAL = 2,

class Action:
    def __init__(self, name: str, type: ActionTypes, category: ActionCategories,
                points_given: int | float, points_used: int, description: str,
                requirement_level: int) -> None:
        self.name = name
        self.type = type
        self.category = category
        # For attack, points = base attack for move
        # For health, points = percentage of health healed
        self.points_given = points_given
        self.points_used = points_used
        self.description = description
        # Requirement level needs to match for the player to be able to use the action
        self.requirement_level = requirement_level