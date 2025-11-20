import random

from battle_types.action import Action
from battle_types.initalise_actions import ActionTypes

class Entity:
    def __init__(self, health: int, attack: int, name: str, 
                 crit_damage: float, crit_rate: float, speed: int, actions: list) -> None:
        self.health = health
        self.attack = attack
        self.name = name
        self.crit_damage = crit_damage
        self.crit_rate = crit_rate
        self.speed = speed
        self.actions = actions
    
    def print_basic_stats(self) -> None:
        print("--{name}--".format(name = self.name))
        print(f"{f"Health: {self.health}":20s}Attack:{self.attack}")
    
    def print_all_stats(self) -> None:
        self.print_basic_stats()
        print(f"{f"Crit Rate: {self.crit_rate:.2f}":20s}Crit Damage:{self.crit_damage}")
        print(f"Speed: {self.speed}")
    
    def print_crit_hit(self) -> None:
        print("Critical hit!")
    
    def print_attack(self, action: Action, opponent: Entity) -> None:
        pass

    def print_heal(self, action: Action) -> None:
        pass
    
    def print_damaged(self, damage: int) -> None:
        pass

    # Returns array (damage, is_crit)
    def calc_damage(self, action: Action, attacker: Entity) -> list:
        is_crit = False
        damage = attacker.attack + action.points

        # See if attacker will do a crit attack
        number: int = random.randint(1, 100)
        if (number <= attacker.crit_rate * 100):
            # Crit attack
            is_crit = True
            damage = int(damage * attacker.crit_damage)

        # Otherwise, damage = attack
        return [damage, is_crit]

    def use_attack(self, attack: Action, opponent: Entity):
        damage = self.calc_damage(attack, self)

        opponent.health -= damage[0]
        
        self.print_attack(attack, opponent)

        if damage[1]:
            self.print_crit_hit()
        
        opponent.print_damaged(damage[0])

    def use_heal(self, heal: Action, user: Entity):
        pass

    def use_action(self, action: Action, opponent: Entity):
        if (action.type == ActionTypes.ATTACK):
            self.use_attack(action, opponent)