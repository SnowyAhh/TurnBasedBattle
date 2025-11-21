from battle_types.action import *
from battle_types.player import *

# Initalise actions
# Dictionary format: category_type_name
action_list = {
    "physical_attack_punch": Action("Punch", ActionTypes.ATTACK, 10, "Punch the enemy"),
    "physical_attack_stab": Action("Stab", ActionTypes.ATTACK, 15, "Stab the enemy"),
    "magic_attack_air_blast": Action("Air blast", ActionTypes.ATTACK, 15, "Blast the enemy with air"),
    "magic_health_heal": Action("Heal", ActionTypes.HEALTH, 0.25, "Heals self")
}