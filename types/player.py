from types.entity import Entity

class Player(Entity):
    def __init__(self) -> None:
        # Set starting stats
        starting_health = 100
        starting_attack = 20
        player_name = "You"
        super().__init__(starting_health, starting_attack, player_name)
    
    def print_attack(self, opponent: Entity) -> None:
        print("{name} attack {oppo}!".format(name = self.name, oppo = opponent.name))

    def print_damaged(self, damage: int) -> None:
        print("{name} take {dmg} damage!".format(name = self.name, dmg = damage))