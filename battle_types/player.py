from battle_types.entity import Entity
from battle_types.initalise_items import item_list

class Player(Entity):
    def __init__(self) -> None:
        # Set starting stats
        starting_health = 100
        starting_attack = 20
        player_name = "You"
        self.items = self.initalise_items()
        super().__init__(starting_health, starting_attack, player_name)
    
    def initalise_items(self) -> list:
        i_list = [
                    [item_list.get("sml_hp_potion"), 5], 
                    [item_list.get("med_hp_potion"), 3]
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