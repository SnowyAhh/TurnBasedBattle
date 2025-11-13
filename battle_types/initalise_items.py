from battle_types.item import *

# Initalise items
# Dictionary format: category_type_size
item_list = {
    "potion_hp_sml": Item("Small health potion", ItemTypes.HEALTH, 15, "Heals 15 hp"),
    "potion_hp_med": Item("Medium health potion", ItemTypes.HEALTH, 30, "Heals 30 hp"),
    "potion_hp_lrg": Item("Large health potion", ItemTypes.HEALTH, 50, "Heals 50 hp"),
    "potion_atk_sml": Item("Small strength potion", ItemTypes.ATTACK, 5, "Increases attack by 5"),
    "potion_atk_med": Item("Medium strength potion", ItemTypes.ATTACK, 10, "Increases attack by 10"),
    "potion_atk_lrg": Item("Large strength potion", ItemTypes.ATTACK, 20, "Increases attack by 20"),
    "potion_rate_sml": Item("Small crit rate potion", ItemTypes.CRIT_RATE, 0.1, "Increases crit rate by 0.1"),
    "potion_rate_med": Item("Medium crit rate potion", ItemTypes.CRIT_RATE, 0.2, "Increases crit rate by 0.2"),
    "potion_rate_lrg": Item("Large crit rate potion", ItemTypes.CRIT_RATE, 0.3, "Increases crit rate by 0.3"),
    "potion_cdmg_sml": Item("Small crit damage potion", ItemTypes.CRIT_DAMAGE, 0.1, "Increases crit damage by 0.1"),
    "potion_cdmg_med": Item("Medium crit damage potion", ItemTypes.CRIT_DAMAGE, 0.40, "Increases crit rate by 0.40"),
    "potion_cdmg_lrg": Item("Large crit damage potion", ItemTypes.CRIT_DAMAGE, 1.0, "Increases crit rate by 1.0"),
}