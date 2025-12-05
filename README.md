# TurnBasedBattle
A prototype of a turn-based fight written in Python.

User stories can be found in the [project board](https://github.com/users/SnowyAhh/projects/3).

# Formulas
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

## Level exprience
To calculate the amount of experience needed to level up at level *n*:
int(100 + 100 * (n - 1)/2)
E.g. Level 1 to 2 requires 100 exp, 2 to 3 is 150 exp, etc

## Experience from defeating enemies
To calculate the experience gained from defeating an enemy:
enemy.max_health / 2