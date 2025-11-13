from battle_types.entity import Entity
from battle_types.initalise_items import item_list
from battle_types.item import ItemTypes

class Player(Entity):
    def __init__(self) -> None:
        # Set starting stats
        starting_health = 100
        starting_attack = 20
        player_name = "You"
        starting_crit_damage_percentage = 1.5
        starting_crit_rate_percentage = 0.25
        self.items = self.initalise_items()
        super().__init__(starting_health, starting_attack, player_name, 
                         starting_crit_damage_percentage, 
                         starting_crit_rate_percentage)
    
    def initalise_items(self) -> list:
        i_list = [
                    [item_list.get("potion_hp_sml"), 5], 
                    [item_list.get("potion_hp_med"), 3],
                    [item_list.get("potion_atk_sml"), 3],
                    [item_list.get("potion_atk_lrg"), 3],
                    [item_list.get("potion_rate_med"), 5],
                    [item_list.get("potion_rate_lrg"), 3],
                    [item_list.get("potion_cdmg_sml"), 4],
                    [item_list.get("potion_cdmg_lrg"), 2],
                ]
    
        return i_list
    
    def decrease_item(self, index) -> None:
        self.items[index][1] -= 1

        # Remove item from list if its quantity is 0
        if (self.items[index][1] == 0):
            self.items.pop(index)

    def print_attack(self, opponent: Entity) -> None:
        print("{name} attack {oppo}!".format(name = self.name, oppo = opponent.name))

    def print_damaged(self, damage: int) -> None:
        print("{name} take {dmg} damage!".format(name = self.name, dmg = damage))

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
            case _:
                raise ValueError("Invalid choice")

    