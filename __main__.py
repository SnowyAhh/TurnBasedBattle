from battle_types.player import Player
from battle import Battle
# File for getting terminal input and showing terminal output
def main():
    player = Player()
    battle = Battle(player)
    battle.battle()

if __name__ == "__main__":
    main()