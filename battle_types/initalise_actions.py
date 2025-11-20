from battle_types.action import *
from battle_types.player import *

# Initalise actions
# Dictionary format: category_type_name
action_list = {
    "physical_attack_punch": Action("Punch", ActionTypes.ATTACK, 10, "Punch the enemy"),
    "physical_attack_stab": Action("Stab", ActionTypes.ATTACK, 15, "Stab the enemy")
}