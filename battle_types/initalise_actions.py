from battle_types.action import *

# Initalise actions
# Dictionary format: category_type_name
action_list = {
    "physical_attack_punch": Action("Punch", ActionTypes.ATTACK, ActionCategories.PHYSICAL, 10, 5, "Punch the enemy"),
    "physical_attack_stab": Action("Stab", ActionTypes.ATTACK, ActionCategories.PHYSICAL, 15, 10, "Stab the enemy"),
    "magical_attack_air_blast": Action("Air blast", ActionTypes.ATTACK, ActionCategories.MAGICAL, 15, 15, "Blast the enemy with air"),
    "magical_health_heal": Action("Heal", ActionTypes.HEALTH, ActionCategories.MAGICAL, 0.25, 20, "Heals self"),
    "other_recover_wait": Action("Wait", ActionTypes.RECOVER, ActionCategories.PHYSICAL, 20, 0, "Use up a round to recover stamina and mana") 
}

action_values_list = list(action_list.values())