# TurnBasedBattle
A prototype of a turn-based fight written in Python.

User stories can be found in the [project board](https://github.com/users/SnowyAhh/projects/3).

# Formulas for actions
## Attacks
For non-critical attack action, damage is calculated by:
player.attack + action.points_given

For critical attack action, damage is calculated by:
(player.attack + action.points_given) * player.crit_damage

## Healing
For non-critical heals, hp healed is calculated by:
player.health * action.points_given

For critical heals, hp healed is calculated by:
(player.health * action.points_given) * player.crit_damage

## Stamina/Mana
To calculate the chance of using a move when there is not enough stamina or mana is:
(amount of stamina/mana left) / (amount of stamania/mana needed)