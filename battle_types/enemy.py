from battle_types.entity import Entity
from battle_types.player import Player

class Enemy(Entity):
    def print_attack(self, opponent: Entity) -> None:
        if isinstance(opponent, Player):
            print("{name} attacks you!".format(name = self.name))
        else: 
            print("{name} attacks {oppo}!".format(name = self.name, oppo = opponent.name))

    def print_damaged(self, damage: int) -> None:
        print("{name} takes {dmg} damage!".format(name = self.name, dmg = damage))

