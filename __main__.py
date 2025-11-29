from battle_types.player import Player
from battle_types.initalise_items import items_values_list
from battle import Battle
from util import get_menu_input
import random
import time

def print_menu_and_get_input(stage: int) -> str:
    accepted = ["1", "Q", "q"]

    print(f"---Stage {stage}---")
    print("Choose your action:")
    print("1. Move to new area")
    print("Q: Quit game")

    return get_menu_input(accepted)

# def get_new_item() -> None:
#     item = items_values_list[random.randint(0, len(items_values_list) - 1)]

def chance_encounter(player: Player) -> None:
    # Encountering an enemy is be 50%, gaining an item is 33.33%, and nothing is 16.67%
    # Out of 6, enemy is 1-3, item is 4-5, and nothing is 6
    chance = random.randint(1, 6)

    print("Moving to new area...")
    time.sleep(1)

    if (chance <= 3):
        # Enemy
        Battle(player).battle()
    elif (chance <= 5):
        # Item
        print("Found an item!")
    else:
        # Nothing
        print("You found nothing here")

def quit() -> None:
    print("Goodbye!")

def main():
    player = Player()
    stage = 0

    # Moving outside of battles
    choice = ""
    while (choice != "q" or "Q"):
        stage += 1
        input = print_menu_and_get_input(stage)

        match input:
            case "1":
                chance_encounter(player)
            case "Q" | "q":
                quit()
                return
            case _:
                raise ValueError("Invalid input")
        


if __name__ == "__main__":
    main()