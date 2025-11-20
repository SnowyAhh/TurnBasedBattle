import random

from battle_types.entity import Entity
from battle_types.player import Player
from battle_types.action import Action

class Enemy(Entity):
    def choose_action(self) -> Action:
        num_moves = len(self.actions)

        return self.actions[random.randint(0, num_moves - 1)]

    def print_attack(self, action: Action, opponent: Entity) -> None:
        if isinstance(opponent, Player):
            print("{name} uses {action} on you!".format(name = self.name, action = action.name))
        else: 
            print("{name} uses {action} on {oppo}!".format(name = self.name, action = action.name, oppo = opponent.name))

    def print_damaged(self, damage: int) -> None:
        print("{name} takes {dmg} damage!".format(name = self.name, dmg = damage))
    
    def print_heal(self, action: Action, healed: int, is_crit: bool) -> None:
        print("{name} uses {action}".format(
            name = self.name, action = action.name
        ))

        if is_crit:
            print("Received extra health!")
        
        print("Healed {hp} hp!".format(hp = healed))

