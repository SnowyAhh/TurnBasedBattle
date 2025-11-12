class Entity:
    def __init__(self, health: int, attack: int, name: str, 
                 crit_damage: float, crit_rate: float) -> None:
        self.health = health
        self.attack = attack
        self.name = name
        self.crit_damage = crit_damage
        self.crit_rate = crit_rate
    
    def print_stats(self) -> None:
        print("--{name}--".format(name = self.name))
        print("   Health:", self.health, "\t", "Attack:", self.attack)
    
    def print_crit_hit(self) -> None:
        print("Critical hit!")
    
    def print_attack(self, opponent) -> None:
        pass
    
    def print_damaged(self, damage: int) -> None:
        pass