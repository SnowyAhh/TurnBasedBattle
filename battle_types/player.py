from battle_types.entity import Entity
from battle_types.initalise_items import item_list
from battle_types.item import ItemTypes
from battle_types.initalise_actions import action_list
from battle_types.action import Action

class Player(Entity):
    def __init__(self) -> None:
        # Set starting stats
        self.items = self.initalise_items()
        super().__init__(health=100, attack=20, name="You", 
                         crit_damage=1.5, crit_rate=0.25, speed=100, 
                         actions=self.initalise_actions(), stamina=100, mana=100)
    
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
                    [item_list.get("potion_speed_lrg"), 4],
                ]
    
        return i_list
    
    def initalise_actions(self) -> list:
        a_list = [
            action_list.get("physical_attack_punch"),
            action_list.get("physical_attack_stab"),
            action_list.get("magical_health_heal"),
            action_list.get("magical_attack_air_blast")
        ]

        return a_list

    def decrease_item(self, index) -> None:
        self.items[index][1] -= 1

        # Remove item from list if its quantity is 0
        if (self.items[index][1] == 0):
            self.items.pop(index)

    def print_attack(self, action: Action, opponent: Entity) -> None:
        print("{name} use {action} on {oppo}!".format(
            name = self.name, action = action.name, oppo = opponent.name
        ))

    def print_damaged(self, damage: int) -> None:
        print("{name} take {dmg} damage!".format(name = self.name, dmg = damage))
    
    def print_heal(self, action: Action, healed: int, is_crit: bool) -> None:
        print("{name} use {action}".format(
            name = self.name, action = action.name
        ))

        if is_crit:
            print("Received extra health!")
        
        print("Healed {hp} hp!".format(hp = healed))

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
            case _:
                raise ValueError("Invalid choice")
    