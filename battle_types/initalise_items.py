from battle_types.item import *

# Initalise items
item_list = {
    "sml_hp_potion": Item("Small health potion", ItemTypes.HEALTH, 15, "Heals 15 hp"),
    "med_hp_potion": Item("Medium health potion", ItemTypes.HEALTH, 30, "Heals 30 hp"),
    "lrg_atk_potion": Item("Large health potion", ItemTypes.HEALTH, 50, "Heals 50 hp"),
    "sml_atk_potion": Item("Small strength potion", ItemTypes.ATTACK, 5, "Increases attack by 5"),
    "med_atk_potion": Item("Medium strength potion", ItemTypes.ATTACK, 10, "Increases attack by 10"),
    "lrg_atk_potion": Item("Large strength potion", ItemTypes.ATTACK, 20, "Increases attack by 20"),
    "sml_rate_potion": Item("Small crit rate potion", ItemTypes.CRIT_RATE, 0.1, "Increases crit rate by 0.1"),
    "med_rate_potion": Item("Medium crit rate potion", ItemTypes.CRIT_RATE, 0.2, "Increases crit rate by 0.2"),
    "lrg_rate_potion": Item("Large crit rate potion", ItemTypes.CRIT_RATE, 0.3, "Increases crit rate by 0.3"),
    "sml_cdmg_potion": Item("Small crit damage potion", ItemTypes.CRIT_DAMAGE, 0.1, "Increases crit damage by 0.1"),
    "med_cdmg_potion": Item("Medium crit damage potion", ItemTypes.CRIT_DAMAGE, 0.40, "Increases crit rate by 0.40"),
    "lrg_cdmg_potion": Item("Large crit damage potion", ItemTypes.CRIT_DAMAGE, 1.0, "Increases crit rate by 1.0"),
}