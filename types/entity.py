class Entity:
    def __init__(self, health, attack, name) -> None:
        self.health = health
        self.attack = attack
        self.name = name
    
    def print_stats(self) -> None:
        print("--{name}--".format(name = self.name))
        print("Health:", self.health, "\t", "Attack:", self.attack)