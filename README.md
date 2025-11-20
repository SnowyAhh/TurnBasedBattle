# TurnBasedBattle
A prototype of a turn-based fight written in Python.

User stories can be found in the [project board](https://github.com/users/SnowyAhh/projects/3).

# Formulas for actions
## Attacks
For non-critical attack action, damage is calculated by:
player.attack + action.points

For critical attack action, damage is calculated by:
(player.attack + action.points) * player.crit_damage

## Healing
For non-critical heals, hp healed is calculated by:
player.health * action.points

For critical heals, hp healed is calculated by:
(player.health * action.points) * player.crit_damage