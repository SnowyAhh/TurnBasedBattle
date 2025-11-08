from battle_types.item import *

# Initalise items
item_list = {
    "sml_hp_potion": Item("Small health potion", ItemTypes.HEALTH, 15, "Heals 15 hp"),
    "med_hp_potion": Item("Medium health potion", ItemTypes.HEALTH, 30, "Heals 30 hp"),
    "sml_atk_potion": Item("Small strength potion", ItemTypes.ATTACK, 5, "Increases attack by 5"),
    "med_atk_potion": Item("Medium strength potion", ItemTypes.ATTACK, 10, "Increases attack by 10"),
    "lrg_atk_potion": Item("Large strength potion", ItemTypes.ATTACK, 20, "Increases attack by 20"),
}