from battle_types.player import Player
from battle_types.initalise_items import items_values_list
from battle import Battle
from util import get_menu_input
import random
import time

class Travel:
    def __init__(self) -> None:
        self.player = Player()
        self.stage = 1

    def print_start(self) -> None:
        print("Welcome to turn based battle!")

    def print_menu(self, stage: int) -> None:
        print(f"\n---Stage {stage}---")
        print("--Choose your action--")
        print(f"{"1. Move to new area":30s}2. Use Item")
        print(f"{"3. Check stats":30s}Q. Quit game")

    def get_new_item(self) -> None:
        item = items_values_list[random.randint(0, len(items_values_list) - 1)]
        quantity = random.randint(1, 3)

        print(f"Found {quantity} {item.name}(s)!")

        self.player.increase_item(item, quantity)
    
    def regenerate_stamina_and_mana(self) -> None:
        # Reset stamina and mana
        self.player.stamina = self.player.max_stamina
        self.player.mana = self.player.max_mana

    def chance_encounter(self) -> bool:
        # Encountering an enemy is be 50%, gaining an item is 33.33%, and nothing is 16.67%
        # Out of 6, enemy is 1-3, item is 4-5, and nothing is 6
        chance = random.randint(1, 6)

        if (chance <= 3):
            # Enemy
            return Battle(self.player).battle()
        elif (chance <= 5):
            # Item
            self.get_new_item()
            return True
        else:
            # Nothing
            print("You found nothing here")
            return True
    
    def chance_encounter_use_item(self) -> bool:
        # Chance of encountering an enemy after using an item
        chance = random.randint(1, 6)

        if (chance <= 3):
            # Enemy
            print("A surprise attack!")

            return Battle(self.player).battle()

        # Else nothing happens
        return True

    def print_quit(self) -> None:
        print("Your travels have ended!")

    def travel(self) -> None:
        menu_choices_list = ["1", "2", "3", "Q", "q"]

        # Moving outside of battles
        self.print_start()
        survived = True
        while (survived):
            self.print_menu(self.stage)
            input = get_menu_input(menu_choices_list)

            match input:
                case "1":
                    print("Moving to new area...")
                    time.sleep(1)

                    survived = self.chance_encounter()
                case "2":
                    success = self.player.get_item_choice()

                    if not success:
                        continue
                    else:
                        survived = self.chance_encounter_use_item()
                case "3":
                    self.player.print_all_stats()
                    print()

                    # Wait for the player to choose to go back
                    print("Go back now? (Y)")
                    get_menu_input(["Y", "y"])
                    continue
                case "Q" | "q":
                    break
                case _:
                    raise ValueError("Invalid input")

            self.regenerate_stamina_and_mana()
            self.stage += 1

        self.print_quit()
        

