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

    def print_menu_and_get_input(self, stage: int) -> str:
        accepted = ["1", "2", "Q", "q"]

        print(f"---Stage {stage}---")
        print("Choose your action:")
        print("1. Move to new area")
        print("2. Check status")
        print("Q: Quit game")

        return get_menu_input(accepted)

    def get_new_item(self) -> None:
        item = items_values_list[random.randint(0, len(items_values_list) - 1)]
        quantity = random.randint(1, 3)

        print(f"Found {quantity} {item.name}(s)!")

        self.player.increase_item(item, quantity)

    def chance_encounter(self) -> None:
        # Encountering an enemy is be 50%, gaining an item is 33.33%, and nothing is 16.67%
        # Out of 6, enemy is 1-3, item is 4-5, and nothing is 6
        chance = random.randint(1, 6)

        print("Moving to new area...")
        time.sleep(1)

        if (chance <= 3):
            # Enemy
            Battle(self.player).battle()
        elif (chance <= 5):
            # Item
            self.get_new_item()
        else:
            # Nothing
            print("You found nothing here")

    def quit(self) -> None:
        print("Goodbye!")

    def travel(self) -> None:
        # Moving outside of battles
        choice = ""

        self.print_start()
        while (choice != "q" or "Q"):
            input = self.print_menu_and_get_input(self.stage)

            match input:
                case "1":
                    self.chance_encounter()
                case "2":
                    self.player.print_all_stats()
                    print()

                    continue
                case "Q" | "q":
                    quit()
                    return
                case _:
                    raise ValueError("Invalid input")

            self.stage += 1
        

