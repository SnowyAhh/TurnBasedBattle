import random

from battle_types.entity import Entity
from battle_types.enemy import Enemy
from battle_types.player import Player
from battle_types.initalise_actions import action_list
from battle_types.action import Action

class Battle:
    # Battle file, shows moves, damage, health
    def __init__(self, player: Player) -> None:
        self.round = 1
        self.enemy = self.generate_enemy()
        self.player = player

    # Randomises an enemy
    def generate_enemy(self) -> Enemy:
        # For now, it'll generate a set stat enemy
        a_list = [
            action_list.get("physical_attack_punch"),
            action_list.get("physical_attack_stab"),
            action_list.get("magical_health_heal"),
            action_list.get("other_recover_wait")
        ]

        enemy = Enemy(health=100, attack=10, name="Thief", 
                      crit_damage=1.5, crit_rate=0.2, speed=100, actions=a_list,
                      stamina=100, mana=100)
        return enemy

    # Menu prints
    def print_start(self) -> None:
        print("A {e} suddenly appears!".format(e = self.enemy.name))

    def print_menu(self) -> None:
        print("\n---Round {number}---".format(number = self.round))
        self.enemy.print_basic_stats()
        self.player.print_basic_stats()
        print("--Choose your move--")
        print(f"{"1. Act":20s}2. Use Item")
        print(f"{"3. Check stats":20s}4. Run away")
    
    def print_stats(self) -> None:
        print("Stats:")
        self.enemy.print_all_stats()
        self.player.print_all_stats()
        print()
        
        # Wait for the player to choose to go back
        print("Go back now? (Y)")
        self.get_menu_input(["Y", "y"])

    # Check input
    def get_menu_input(self, accepted: list[str]) -> str:
        choice = ""
        choice = input()
        while choice not in accepted:
            print("Invalid choice, try again: ")
            choice = input()
        return choice
    
    # Action
    def get_action(self) -> str:
        print("\nChoose an action, or q to go back")
    
        num_arr = self.player.print_actions()
        num_arr.append("Q")
        num_arr.append("q")
        
        return self.get_menu_input(num_arr)

    def calc_damage(self, attacker: Entity) -> int:
        damage = attacker.attack

        # See if attacker will do a crit attack
        number: int = random.randint(1, 100)
        if (number <= attacker.crit_rate * 100):
            # Crit attack
            damage = int(damage * attacker.crit_damage)

        # Otherwise, damage = attack
        return damage

    def player_acts_first(self, player_action: Action, enemy_action: Action) -> bool:
        self.player.use_action(player_action, self.enemy)

        if self.enemy.health <= 0:
            return True
        
        self.enemy.use_action(enemy_action, self.player)

        return True
    
    def enemy_acts_first(self, player_action: Action, enemy_action: Action) -> bool:
        self.enemy.use_action(enemy_action, self.player)

        if self.player.health <= 0:
            return True
        
        self.player.use_action(player_action, self.enemy)

        return True

    # Speed is incorporated into attacks
    def speed_attack(self) -> bool:
        # Get action first
        choice = self.get_action()

        if (choice == "Q" or choice == "q"):
            return False
        
        player_action = self.player.actions[int(choice) - 1]

        # Get enemy action
        enemy_action = self.enemy.choose_action()

        if (self.player.speed < self.enemy.speed):
            return self.enemy_acts_first(player_action, enemy_action)
        elif (self.player.speed > self.enemy.speed):
            return self.player_acts_first(player_action, enemy_action)
        else: 
            # player.speed == enemy.speed
            # 50/50 chance between the two on who goes first
            number: int = random.randint(1, 2)

            if number == 1:
                return self.enemy_acts_first(player_action, enemy_action)
            else:
                return self.player_acts_first(player_action, enemy_action)


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
            print("\t{num}. {name} x{quantity} - {description}".format(
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
        return self.player.use_item(index)


    # Fight function
    def battle(self) -> None:
        # Inputs accepted while choose for menu
        menu_choices_list = ["1", "2", "3", "4"]
        
        self.print_start()
        enemy_has_already_attacked = False
        while (self.enemy.health > 0 and self.player.health > 0):
            self.print_menu()
            choice = self.get_menu_input(menu_choices_list)

            match choice:
                case "1":
                    enemy_has_already_attacked = self.speed_attack()

                    # Player chose to quit out of action menu
                    if not enemy_has_already_attacked:
                        continue
                case "2":
                    # Use item
                    success = self.use_item()

                    if not success:
                        continue
                case "3":
                    # Check stats
                    self.print_stats()

                    continue
                case "4":
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
            
            if (self.enemy.health <= 0 or self.player.health <= 0):
                break
            
            # Attacks only if player has successfully used item or failed to run away
            if not enemy_has_already_attacked:
                action = self.enemy.choose_action()
                self.enemy.use_action(action, self.player)

            # Recover stamina and mana for enemy and player at the end of the round
            print("--End of turn recovery--")
            self.player.recover_stamina_and_mana_partial(5, 5)
            self.enemy.recover_stamina_and_mana_partial(5, 5)
            
            enemy_has_already_attacked = False

            self.round += 1
        
        if (self.enemy.health <= 0):
            print("You've defeated {e}".format(e = self.enemy.name))
        elif (self.player.health <= 0):
            print("You've been defeated by {e}".format(e = self.enemy.name))
            