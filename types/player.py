from types.entity import Entity

class Player(Entity):
    def __init__(self) -> None:
        # Set starting stats
        starting_health = 100
        starting_attack = 10
        player_name = "You"
        super().__init__(starting_health, starting_attack, player_name)