from enemy_data import ENEMY_SPAWN_DATA

#map and screen structure
ROWS = 15
COLS = 24
TILE_SIZE = 65
SIDE_PANEL = 270
SCREEN_WIDTH = COLS * TILE_SIZE
SCREEN_HEIGHT = ROWS * TILE_SIZE
FPS = 60

#player starting resources
PLAYER_HP = 100
SCORE_VALUE_PER_HP_ON_WIN = 10
PLAYER_MONEY = 100

LEVEL_COMPLETE_REWARD = 25

level_count = 0
level_group_count = 0
for i in range(len(ENEMY_SPAWN_DATA)):
    level_group_count += 1
    level_count += len(ENEMY_SPAWN_DATA[i])

TOTAL_LEVELS = level_count
TOTAL_GROUPS = level_group_count

FAST_FORWARD_SPEED = 10

UNDO_MAX = 10

TURRET_SELL_VALUE = 0.75 #percentage of total money spent refunded

VULNERABILITY_MULT = 1.5 #higher values make some towers more effective
RESISTANCE_MULT = 0.7 #higher values make some towers less effective
ENEMY_SPEED_CAP = 4.25 #enemy speed increases per level, up to this cap
ENEMY_ARMOR_CAP = 0.5 #enemy armor increases per level, up to this cap

EFFECTS = {
    "dmg_over_time": {"dmg_mult": .13, "duration": 7500, "interval_time": 150, 'text': 'DoT'}, # higher dmg_mult, higher damage done based on tower's base dmg
    "slow": {"speed_mult": .7, "duration": 4000, 'text': "Slow"}, # the lower speed_mult, the slower the enemies go, 0 for stun
    "stun": {"cooldown": 7000,"duration": 2500, 'text': "Stun"}, #cooldown is how many millisec an enemy is immune to stun after a stun effect falls off
    "armor_pen": {"armor_mult": 1.5, "duration": 0, 'text': "Armor Pen"}, # the higher armor_mult, the more dmg done
}
ARMOR_PEN_EFFECTIVENESS = 1.1 #high numbers are more effective, 1 for no change, 0 to nullify the effect, negative values heal the target, values between 0 and 1 (exclusive) to dampen the effect

ENEMY_CATEGORIES = ['animal', 'construct', 'dragon', 'goblin', 'humanoid', 'monstrous', 'undead'] #used to convert indexes to keys for hash table look ups in certain cases

DMG_TYPES = {"electric": "Electric", "fire": "Fire", "frost": "Cold", "heavy": "Heavy", "pierce": "Piercing", "poison": "Poison", "ranged": "Ranged", "slash": "Slashing"} #used to aid in draw_text UI applications

TURRET_LIST = ["archer", "crossbowman", "melee", "siege", "sniper", "fire", "frost", "poison", "electric"] #used to convert indexes to keys for hash table look ups in certain cases

#difficulty scaling functions, find these used in enemy.py under effect implementation function
def DIFFICULTY_HP_POWER(level):
    return (1 + level/TOTAL_LEVELS)

def DIFFICULTY_SPEED_ADD(level):
    return ((level/TOTAL_LEVELS)*2)

def DIFFICULTY_ARMOR_MULT(level):
    return (1 + (level/TOTAL_LEVELS)*3)

# def DIFFICULTY_VALUE_MULT(level):
#     return (1 + (level/TOTAL_LEVELS)*1.5)

def DIFFICULTY_VALUE_MULT(level): #testing this instead to give less money early on and more later;
    return ((15**((level+1)/TOTAL_LEVELS))/(2**((level+1+TOTAL_LEVELS)/TOTAL_LEVELS))/1.2)