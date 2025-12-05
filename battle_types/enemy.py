import random

from battle_types.entity import Entity
from battle_types.player import Player
from battle_types.action import Action
from battle_types.initalise_actions import action_list, action_values_list

enemy_names = [
    "Thief",
    "Pirate",
    "Mage",
    "Warrior"
]

class Enemy(Entity):
    @staticmethod
    def generate_random_enemy() -> Enemy:
        a_list = [
            action_list.get("other_recover_wait")
        ]

        # Add one to four moves
        for i in range(0, random.randint(1, 5)):
            action = action_values_list[i]

            if action in a_list:
                i -= 1
                continue
            
            a_list.append(action)

        return Enemy(health=random.randint(50, 200), 
                      attack=random.randint(5, 20), 
                      name=enemy_names[random.randint(0, len(enemy_names) - 1)], 
                      crit_damage=1 + random.random(), 
                      crit_rate=random.random(), 
                      speed=random.randint(50, 150),
                      actions=a_list, 
                      stamina=random.randint(50, 200), 
                      mana=random.randint(50, 200))

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
    
    def print_heal(self, action: Action) -> None:
        print(f"{self.name} uses {action.name}")
    
    def print_not_enough_stamina(self, action: Action) -> None:
        print(f"{self.name} tries to use {action.name} but they don't have enough stamina")
    
    def print_not_enough_mana(self, action: Action) -> None:
        print(f"{self.name} tries to use {action.name} but they don't have enough mana")
    
    def print_wait(self) -> None:
        print(f"{self.name} waits a turn")

