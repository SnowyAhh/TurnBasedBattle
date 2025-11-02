class Entity:
    def __init__(self, health, attack, name) -> None:
        self.health = health
        self.attack = attack
        self.name = name
    
    def print_stats(self) -> None:
        print("--{name}--".format(name = self.name))
        print("Health:", self.health, "\t", "Attack:", self.attack)
    
    def print_attack(self, opponent) -> None:
        pass
    
    def print_damaged(self, damage: int) -> None:
        pass