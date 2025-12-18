from battle_types.action import *

# Initalise actions
# Dictionary format: category_type_name
action_list = {
    "physical_attack_punch": Action("Punch", ActionTypes.ATTACK, ActionCategories.PHYSICAL, 10, 5, "Punch the enemy", 1),
    "physical_attack_stab": Action("Stab", ActionTypes.ATTACK, ActionCategories.PHYSICAL, 15, 20, "Stab the enemy", 3),
    "physical_attack_swing": Action("Swing", ActionTypes.ATTACK, ActionCategories.PHYSICAL, 20, 30, "Swing your weapon at the enemy", 6),
    "magical_attack_fireball": Action("Fireball", ActionTypes.ATTACK, ActionCategories.MAGICAL, 10, 10, "Send a ball of fire at the enemy", 2),
    "magical_attack_air_blast": Action("Air blast", ActionTypes.ATTACK, ActionCategories.MAGICAL, 15, 20, "Blast the enemy with air", 4),
    "magical_health_heal": Action("Heal", ActionTypes.HEALTH, ActionCategories.MAGICAL, 0.25, 20, "Heals self", 5),
    "other_recover_wait": Action("Wait", ActionTypes.RECOVER, ActionCategories.PHYSICAL, 20, 0, "Use up a round to recover stamina and mana", 1), 
}

action_values_list = list(action_list.values())