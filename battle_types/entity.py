import random

from battle_types.action import Action
from battle_types.initalise_actions import *

class Entity:
    def __init__(self, health: int, attack: int, name: str, crit_damage: float,
                crit_rate: float, speed: int, actions: list, stamina: int,
                mana: int) -> None:
        self.health = health
        self.attack = attack
        self.name = name
        self.crit_damage = crit_damage
        self.crit_rate = crit_rate
        self.speed = speed
        self.actions = actions
        self.stamina = stamina
        self.mana = mana
    
    def print_basic_stats(self) -> None:
        print("--{name}--".format(name = self.name))
        print(f"{f"Health: {int(self.health)}":20s}Attack:{int(self.attack)}")
        print(f"{f"Stamina: {int(self.stamina)}":20s}Mana: {int(self.mana)}")
    
    def print_all_stats(self) -> None:
        self.print_basic_stats()
        print(f"{f"Crit Rate: {self.crit_rate:.2f}":20s}Crit Damage:{self.crit_damage}")
        print(f"Speed: {self.speed}")
    
    def print_attack(self, action: Action, opponent: Entity) -> None:
        pass

    def print_heal(self, action: Action, healed: int, is_crit: bool) -> None:
        pass
    
    def print_damaged(self, damage: int) -> None:
        pass

    def print_not_enough_stamina(self, action: Action) -> None:
        pass

    def print_not_enough_mana(self, action: Action) -> None:
        pass

    # Returns array (damage, is_crit)
    def calc_damage(self, action: Action) -> list:
        is_crit = False
        damage = self.attack + action.points_given

        # See if attacker will do a crit attack
        number: int = random.randint(1, 100)
        if (number <= self.crit_rate * 100):
            # Crit attack
            is_crit = True
            damage = int(damage * self.crit_damage)

        # Otherwise, damage = attack
        return [damage, is_crit]

    def use_attack(self, attack: Action, opponent: Entity) -> None:
        damage = self.calc_damage(attack)

        opponent.health -= damage[0]
        
        self.print_attack(attack, opponent)

        if damage[1]:
            print("Critical hit!")
        
        opponent.print_damaged(damage[0])

    # Returns array (healed, is_crit)
    def calc_heal(self, heal: Action) -> list:
        is_crit = False
        healed = int(self.health * heal.points_given)

        # See if user will do a crit heal
        number: int = random.randint(1, 100)
        if (number <= self.crit_rate * 100):
            # Crit heal
            is_crit = True
            healed = int(healed * self.crit_damage)

        return [healed, is_crit]

    def use_heal(self, heal: Action) -> None:
        healed = self.calc_heal(heal)

        self.print_heal(heal, healed[0], healed[1])
        
        self.health += healed[0]

    def use_action(self, action: Action, opponent: Entity) -> None:
        # See if there is enough stamina/mana to do the action
        # Physical uses stamina, magical uses mana
        if (action.category == ActionCategories.PHYSICAL):
            if (self.stamina - action.points_used <= 0):
                # Chance of using it 
                chance = int(self.stamina / action.points_used * 100)
                
                if (random.randint(1, 100) > chance):
                    self.print_not_enough_stamina(action)
                    return

                # Continue and do the action
                self.stamina = 0
            else:
                self.stamina -= action.points_used
        else:
            if (self.mana - action.points_used <= 0):
                # Chance of using it 
                chance = int(self.mana / action.points_used * 100)
                
                if (random.randint(1, 100) > chance):
                    self.print_not_enough_mana(action)
                    return

                # Continue and do the action
                self.mana = 0
            else:
                self.mana -= action.points_used


        if (action.type == ActionTypes.HEALTH):
            self.use_heal(action)
        elif (action.type == ActionTypes.ATTACK):
            self.use_attack(action, opponent)