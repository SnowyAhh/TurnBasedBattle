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
            print(f"{self.name} uses {action.name} on you!")
        else: 
            print(f"{self.name} uses {action.name} on {opponent.name}!")

    def print_damaged(self, damage: int) -> None:
        print(f"{self.name} takes {damage} damage!")
    
    def print_heal(self, action: Action, healed: int, is_crit: bool) -> None:
        print(f"{self.name} uses {action.name}")

        if is_crit:
            print("Received extra health!")
        
        print(f"Healed {healed} hp!")
    
    def print_not_enough_stamina(self, action: Action) -> None:
        print(f"{self.name} tries to use {action.name} but they don't have enough stamina")
    
    def print_not_enough_mana(self, action: Action) -> None:
        print(f"{self.name} tries to use {action.name} but they don't have enough mana")
    
    def print_wait(self) -> None:
        print(f"{self.name} waits a turn")

