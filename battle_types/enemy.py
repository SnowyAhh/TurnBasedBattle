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
            print("{name} used {action} on {oppo}!".format(name = self.name, action = action.name, oppo = opponent.name))

    def print_damaged(self, damage: int) -> None:
        print("{name} takes {dmg} damage!".format(name = self.name, dmg = damage))
    
    def use_attack(self, attack: Action, user: Entity, opponent: Entity):
        damage = self.calc_damage(attack, user)

        opponent.health -= damage[0]
        
        self.print_attack(attack, opponent)

        if damage[1]:
            super().print_crit_hit()
        
        opponent.print_damaged(damage[0])

