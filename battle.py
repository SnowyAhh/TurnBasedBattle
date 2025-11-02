from types.entity import Entity
from types.enemy import Enemy
from types.player import Player

class Battle:
    # Battle file, shows moves, damage, health
    def __init__(self, player: Player) -> None:
        self.round = 0
        self.enemy = self.generate_enemy()
        self.player = player

    # Randomises an enemy
    def generate_enemy(self) -> Enemy:
        # For now, it'll generate a set stat enemy
        health = 100
        attack = 10
        name = "Thief"
        enemy = Enemy(health, attack, name)
        return enemy

    # Menu prints
    def print_start(self) -> None:
        print("A {e} suddenly appears!".format(e = self.enemy.name))

    def print_menu(self) -> None:
        print("---Round {n}---".format(n = self.round))
        self.enemy.print_stats()
        self.player.print_stats()
        print("--Choose your move--")
        print("1. Attack".ljust(15)) # For future: Print item in same line
        # For future: Print Run away

    # Check input
    def get_menu_input(self, accepted: list[int]) -> int:
        choice = ""
        try :
            choice = int(input())
        except:
            print("Error: Enter a number")
        while choice not in accepted:
            print("Invalid choice, try again: ")
            try:
                choice = int(input())
            except:
                print("Error: Enter a number")
        return int(choice)

    # Attack
    def print_attack(self, attacker: Entity, opponent: Entity, damage: int):
        print("{a} attacks {o}!".format(a = attacker.name, o = opponent.name))
        print("{o} takes {dmg} damage!".format(o = opponent.name, dmg = damage))
    
    def calc_damage(self, damage):
        # For future: Add crit damage and crit rate here
        # Otherwise, damage = attack
        return damage

    def attack(self, attacker: Entity, opponent: Entity):
        damage = self.calc_damage(attacker.attack)
        opponent.health -= damage
        self.print_attack(attacker, opponent, damage)

    # Run away

    # Use items


    # Fight function
    def battle(self) -> None:
        # Inputs accepted while choose for menu
        menu_list_int = [1]
        
        self.print_start()
        while (self.enemy.health != 0 and self.player.health != 0):
            self.round += 1

            # Player turn
            self.print_menu()
            choice = self.get_menu_input(menu_list_int)

            match choice:
                case 1:
                    # Attack
                    self.attack(self.player, self.enemy)
            
            if (self.enemy.health <= 0):
                break
            
            # Enemy turn
            self.attack(self.enemy, self.player)
        
        if (self.enemy.health <= 0):
            print("You've defeated {e}".format(e = self.enemy.name))
        elif (self.player.health <= 0):
            print("You've been defeated by {e}".format(e = self.enemy.name))
            