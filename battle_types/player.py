from battle_types.entity import Entity
from battle_types.initalise_items import item_list
from battle_types.item import ItemTypes, Item
from battle_types.initalise_actions import *
from battle_types.action import Action
from util import get_menu_input

import random

class Player(Entity):
    def __init__(self) -> None:
        # Set starting stats
        self.items = self.initalise_items()
        self.level: int = 1
        self.experience: int = 0
        super().__init__(health=100, attack=20, name="You", 
                         crit_damage=1.5, crit_rate=0.25, speed=100, 
                         actions=self.initalise_actions(), stamina=100, mana=100)

    def initalise_items(self) -> list:
        i_list = [
                    [item_list.get("potion_hp_sml"), 5], 
                    [item_list.get("potion_atk_sml"), 3],
                    [item_list.get("potion_rate_med"), 5],
                    [item_list.get("potion_cdmg_sml"), 4],
                    [item_list.get("potion_speed_lrg"), 4],
                    [item_list.get("potion_stamina_med"), 3],
                    [item_list.get("potion_mana_lrg"), 2],
                ]
    
        return i_list

    def initalise_actions(self) -> list:
        a_list = [
            action_list.get("physical_attack_punch"),
            action_list.get("physical_attack_stab"),
            action_list.get("magical_health_heal"),
            action_list.get("magical_attack_air_blast"),
            action_list.get("other_recover_wait")
        ]

        return a_list
    
    # Override parent function
    def print_all_stats(self) -> None:
        print("--{name}--".format(name = self.name))

        # Part specific to player
        print(f"{f"Level: {self.level}":30s}Experience: {self.experience}")

        print(f"{f"Health: {int(self.health)}":30s}Attack: {int(self.attack)}")
        print(f"{f"Stamina: {int(self.stamina)}":30s}Mana: {int(self.mana)}")
        print(f"{f"Crit Rate: {self.crit_rate:.2f}":30s}Crit Damage: {self.crit_damage:.2f}")
        print(f"Speed: {self.speed}")

    def increase_item(self, item: Item, quantity: int) -> None:
        # Scan item list
        for i in self.items:
            if i[0] == item:
                # If it already in the list, increase quantity
                i[1] += quantity
                return
        
        # Otherwise append
        self.items.append([item, quantity])
        self.items.sort(key=lambda item: (item[0].type, item[0].name))

    def decrease_item(self, index) -> None:
        self.items[index][1] -= 1

        # Remove item from list if its quantity is 0
        if (self.items[index][1] == 0):
            self.items.pop(index)

    def print_attack(self, action: Action, opponent: Entity) -> None:
        print(f"{self.name} use {action.name} on {opponent.name}!")

    def print_damaged(self, damage: int) -> None:
        print(f"{self.name} take {damage} damage!")
    
    def print_heal(self, action: Action, healed: int, is_crit: bool) -> None:
        print(f"{self.name} use {action.name}")

        if is_crit:
            print("Received extra health!")
        
        print(f"Healed {healed} hp!")

    def print_not_enough_stamina(self, action: Action) -> None:
        print(f"You try to use {action.name} but you don't have enough stamina")
    
    def print_not_enough_mana(self, action: Action) -> None:
        print(f"You try to use {action.name} but you don't have enough mana")
    
    def print_actions(self) -> list:
        num_arr = []

        for i in range(len(self.actions)):
            num_arr.append(str(i + 1))
            print("{i}. {name} ({points_used} {cat}) - {description} ({points_given} {type})".format(
                i = i + 1, name = self.actions[i].name, 
                points_used = self.actions[i].points_used,
                cat = "stamina" if self.actions[i].category == ActionCategories.PHYSICAL else "mana",
                description = self.actions[i].description,
                points_given = self.actions[i].points_given if self.actions[i].type != ActionTypes.HEALTH else str(int(self.actions[i].points_given * 100)) + "%",
                type = "attack" if self.actions[i].type == ActionTypes.ATTACK else "health" if self.actions[i].type == ActionTypes.HEALTH else "stamina/mana"
            ))
        
        return num_arr

    def print_recover_stamina(self, amount: int) -> None:
        print(f"You recover {amount} stamina")

    def print_recover_mana(self, amount: int) -> None:
        print(f"You recover {amount} mana")
    
    def print_wait(self) -> None:
        print("You wait a turn")

    def use_health_item(self, index: int) -> bool:
        print("Used {name}. Restored {points} hp!".format(
            name = self.items[index][0].name,
            points = self.items[index][0].points
        ))

        # Increase health
        self.health += self.items[index][0].points
        # Decrease quantity
        self.decrease_item(index)

        return True

    def use_attack_item(self, index: int) -> bool:
        print("Used {name}. Increased attack by {points}!".format(
            name = self.items[index][0].name,
            points = self.items[index][0].points
        ))

        # Increase attack
        self.attack += self.items[index][0].points
        # Decrease quantity
        self.decrease_item(index)

        return True

    def use_rate_item(self, index: int) -> bool:
        # Make sure crit rate hits a max of 1.0
        if (self.crit_rate >= 1.0):
            print("Used {name}. But it failed! Already have max crit rate".format(
                name = self.items[index][0].name
            ))
        elif (self.crit_rate + self.items[index][0].points > 1.0):
            print("Used {name}. Increased crit rate by {points:.2f}!".format(
                name = self.items[index][0].name,
                points = 1.0 - self.crit_rate
            ))

            self.crit_rate = 1.0
        else: 
            print("Used {name}. Increased crit rate by {points}!".format(
                name = self.items[index][0].name,
                points = self.items[index][0].points
            ))

            self.crit_rate += self.items[index][0].points

        # Decrease quantity
        self.decrease_item(index)

        return True

    def use_cdmg_item(self, index: int) -> bool:
        print("Used {name}. Increased crit damage by {points}!".format(
            name = self.items[index][0].name,
            points = self.items[index][0].points
        ))

        # Increase crit damage
        self.crit_damage += self.items[index][0].points
        # Decrease quantity
        self.decrease_item(index)

        return True
    
    def use_speed_item(self, index: int) -> bool:
        print("Used {name}. Increased speed by {points}!".format(
            name = self.items[index][0].name,
            points = self.items[index][0].points
        ))

        # Increase speed
        self.speed += self.items[index][0].points
        # Decrease quantity
        self.decrease_item(index)

        return True
    
    def use_stamina_item(self, index: int) -> bool:
        if (self.stamina >= self.max_stamina):
            print("Used {name}. But it failed! Already have max stamina".format(
                name = self.items[index][0].name
            ))
        elif (self.stamina + self.items[index][0].points > self.max_mana):
            print("Used {name}. Increased stamina by {points}!".format(
                name = self.items[index][0].name,
                points = self.max_stamina - self.stamina
            ))

            self.stamina = self.max_stamina
        else: 
            print("Used {name}. Increased stamina by {points}!".format(
                name = self.items[index][0].name,
                points = self.items[index][0].points
            ))

            self.stamina += self.items[index][0].points

        # Decrease quantity
        self.decrease_item(index)

        return True

    def use_mana_item(self, index: int) -> bool:
        if (self.mana >= self.max_mana):
            print("Used {name}. But it failed! Already have max mana".format(
                name = self.items[index][0].name
            ))
        elif (self.mana + self.items[index][0].points > self.max_mana):
            print("Used {name}. Increased mana by {points}!".format(
                name = self.items[index][0].name,
                points = self.max_mana - self.mana
            ))

            self.mana = self.max_mana
        else: 
            print("Used {name}. Increased mana by {points}!".format(
                name = self.items[index][0].name,
                points = self.items[index][0].points
            ))

            self.mana += self.items[index][0].points

        # Decrease quantity
        self.decrease_item(index)

        return True

    def use_item(self, index: int) -> bool:
        match self.items[index][0].type:
            case ItemTypes.HEALTH:
                return self.use_health_item(index)
            case ItemTypes.ATTACK:
                return self.use_attack_item(index)
            case ItemTypes.CRIT_RATE:
                return self.use_rate_item(index)
            case ItemTypes.CRIT_DAMAGE:
                return self.use_cdmg_item(index)
            case ItemTypes.SPEED:
                return self.use_speed_item(index)
            case ItemTypes.STAMINA:
                return self.use_stamina_item(index)
            case ItemTypes.MANA:
                return self.use_mana_item(index)
            case _:
                raise ValueError("Invalid choice")
    
    def get_item_choice(self) -> bool:
        accepted_list = []
        print("Your Items:")

        if (len(self.items) == 0):
            print("No items available")
            print("Going back to selection: ")
            return False
        
        # Print items
        for i in range(len(self.items)):
            accepted_list.append(str(i + 1))
            print("\t{num}. {name} x{quantity} - {description}".format(
                num = i + 1, 
                name = self.items[i][0].name, 
                quantity = self.items[i][1], 
                description = self.items[i][0].description
            ))

        print("Enter the item number to use it, or q to go back")
        accepted_list.append("q")
        accepted_list.append("Q")
        
        # Get item number
        choice = get_menu_input(accepted_list)

        # Quit from item menu
        if choice == "q" or choice == "Q":
            return False
        
        # Use item
        index = int(choice) - 1
        return self.use_item(index)

    def gain_experience(self, amount: int) -> None:
        # If experience is greater than amount needed to level up, 
        # remove that amount and add remainder to experience

        amount_needed = int(100 + 100 * (self.level - 1) / 2)

        while (self.experience + amount >= amount_needed):
            self.handle_level_up()

            # Use up experience first
            if self.experience != 0:
                amount_needed -= self.experience
                self.experience = 0

            amount -= amount_needed

            amount_needed = int(100 + 100 * (self.level - 1) / 2)

        self.experience += amount
    
    def handle_level_up(self) -> None:
        self.level += 1
        print(f"Leveled up to {self.level}!")

        # Increase stats
        increased_health = random.randint(5, 20)
        increased_attack = random.randint(1, 10)
        increased_stamina = random.randint(5, 20)
        increased_mana = random.randint(5, 20)

        self.health += increased_health
        self.attack += increased_attack
        self.max_stamina += increased_stamina
        self.stamina += increased_stamina
        self.max_mana += increased_mana
        self.mana += increased_mana

        print("Stats increased:")
        print(f"\tHealth: {increased_health}")
        print(f"\tAttack: {increased_attack}")
        print(f"\tMax stamina: {increased_stamina}")
        print(f"\tMax mana: {increased_mana}")