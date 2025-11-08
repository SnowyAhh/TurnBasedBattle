import random

from battle_types.entity import Entity
from battle_types.enemy import Enemy
from battle_types.player import Player
from battle_types.item import ItemTypes

class Battle:
    # Battle file, shows moves, damage, health
    def __init__(self, player: Player) -> None:
        self.round = 1
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
        print("---Round {number}---\n".format(number = self.round))
        self.enemy.print_stats()
        self.player.print_stats()
        print("--Choose your move--")
        print("1. Attack".ljust(15), "2. Use Item")
        print("3. Run away")

    # Check input
    def get_menu_input(self, accepted: list[str]) -> str:
        choice = ""
        choice = input()
        while choice not in accepted:
            print("Invalid choice, try again: ")
            choice = input()
        return choice

    # Attack
    def print_attack(self, attacker: Entity, 
                     opponent: Entity, damage: int) -> None:
        attacker.print_attack(opponent)
        opponent.print_damaged(damage)
        print()
    
    def calc_damage(self, damage) -> int:
        # For future: Add crit damage and crit rate here
        # Otherwise, damage = attack
        return damage

    def attack(self, attacker: Entity, opponent: Entity) -> None:
        damage = self.calc_damage(attacker.attack)
        opponent.health -= damage
        self.print_attack(attacker, opponent, damage)

    # Run away
    def calc_run_away_success(self) -> bool:
        # Run away is 70% chance of success
        number: int = random.randint(1, 10)
        if (number <= 3):
            return False
        else:
            return True

    def get_confirmation(self) -> bool:
        menu_confirmation_list = ["Y", "y", "n", "N"]
        print("Are you sure you want to run? (Y/N)")
        
        choice = self.get_menu_input(menu_confirmation_list)

        if choice == "Y" or choice == "y":
            return True
        elif choice == "N" or choice == "n":
            return False
        
        raise ValueError("Invalid choice")
        
    # Use items
    def use_item(self) -> bool:
        accepted_list = []
        print("Your Items:")

        if (len(self.player.items) == 0):
            print("No items available")
            print("Going back to selection: ")
            return False
        
        # Print items
        for i in range(len(self.player.items)):
            accepted_list.append(str(i + 1))
            print("\t{num}. {name} {quantity} - {description}".format(
                num = i + 1, 
                name = self.player.items[i][0].name, 
                quantity = self.player.items[i][1], 
                description = self.player.items[i][0].description
            ))

        print("Enter the item number to use it, or q to go back")
        accepted_list.append("q")
        accepted_list.append("Q")
        
        # Get item number
        choice = self.get_menu_input(accepted_list)

        # Quit from item menu
        if choice == "q" or choice == "Q":
            return False
        
        # Use item
        index = int(choice) - 1
        if self.player.items[index][0].type is ItemTypes.HEALTH:
            print("Used {name}. Restored {points} hp!".format(
                name = self.player.items[index][0].name,
                points = self.player.items[index][0].points
            ))

            # Increase health
            self.player.health += self.player.items[index][0].points
            # Decrease quantity
            self.player.decrease_item(index)

            return True
        elif self.player.items[index][0].type is ItemTypes.ATTACK:
            print("Used {name}. Increased attack by {points}!".format(
                name = self.player.items[index][0].name,
                points = self.player.items[index][0].points
            ))

            # Increase attack
            self.player.attack += self.player.items[index][0].points
            # Decrease quantity
            self.player.decrease_item(index)

            return True
        else:
            raise ValueError("Invalid choice")


    # Fight function
    def battle(self) -> None:
        # Inputs accepted while choose for menu
        menu_choices_list = ["1", "2", "3"]
        
        self.print_start()
        while (self.enemy.health != 0 and self.player.health != 0):
            # Player turn
            self.print_menu()
            choice = self.get_menu_input(menu_choices_list)

            match choice:
                case "1":
                    # Attack
                    self.attack(self.player, self.enemy)
                case "2":
                    # Use item
                    success = self.use_item()

                    if not success:
                        continue
                case "3":
                    # Run away
                    try:
                        confirmation: bool = self.get_confirmation()
                        if not confirmation:
                            continue
                    except:
                        print("Invalid choice selected")
                        continue

                    success: bool = self.calc_run_away_success()
        
                    if (success):
                        print("Ran away successfully!")
                        break
                    else:
                        print("Failed to run away!")
                case _:
                    print("Invalid choice selected")
                    continue
            
            if (self.enemy.health <= 0):
                break
            
            # Enemy turn
            self.attack(self.enemy, self.player)

            self.round += 1
        
        if (self.enemy.health <= 0):
            print("You've defeated {e}".format(e = self.enemy.name))
        elif (self.player.health <= 0):
            print("You've been defeated by {e}".format(e = self.enemy.name))
            