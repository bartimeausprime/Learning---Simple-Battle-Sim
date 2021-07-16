# Default Parameters Battle Options
player_attack = 0
player_skills = 0
player_defend = 0
# Default Parameters for Player Stats
player_name = 0
player_stats = {"max_hp":0,"curr_hp":0,"max_mp":0,"curr_mp":0,"evasion":0,"crit":0}
# Default Parameters for Player Status
player_status = {"regen":0,"mp_regen":0,"dot":0}
# Default Player Attacks Damage
player_atk =300
# Default Player Skills
player_skills = {"heavy_atk":400,"leech_hp":200,"fireball":500}
#Critical Multiplier
crit_multi = 2
# Default Parameters for Monster Stats
mons_name = 0
mons_stats = {"max_hp":0,"curr_hp":0,"max_mp":0,"curr_mp":0,"evasion":0,"crit":0}
# Default Parameters for Monster Status
mons_status = {"regen":0,"mp_regen":0,"dot":0}
# Default Monster Attacks
mons_atk = 200
# Default Monster Skills
mons_skills = {"smash":400,"poison_lick":100}

#
#
#Import Modules
import math
import time
import click
import random

def loading_screen(load):
    click.clear()
    print(load)
    time.sleep(0.5)
    click.clear()
    print(load+".")
    time.sleep(0.5)
    click.clear()
    print(load+"..")
    time.sleep(0.5)
    click.clear()
    print(load+"...")
    time.sleep(0.5)
    click.clear()
    print(load+"....")
    time.sleep(0.5)
    click.clear()
    print(load+".....")
    time.sleep(0.5)
    click.clear()
    return loading_screen

#Game Start Screen
#done
player_name = str(input("Please enter your player name: "))
player_name_default = player_name
if player_name_default != "":
    player_name_default = player_name
else:
    player_name_default = "Nameless Warrior"
click.clear()
loading_screen("Setting player name")
if player_name == player_name_default:
    print("Warrior",player_name+"!","Welcome to this simple test of a battle simulator with a monster.")
else:
    print(player_name_default+", ""welcome to this simple test of a battle simulator with a monster.")
    player_name = player_name_default
print("")
loading_screen("Your adventure begins")
input("Press enter to continue!")
click.clear()

#Monster Naming
mons_rand_name = 0
def mons_random_name_gen():
    global mons_name
    mons_name_list = {1:"Cupcakes",2:"Muffin Man",3:"Fruit Tart",4:"Crabs"}
    mons_rand_name_draw = random.randint(1,4)
    mons_name = mons_name_list[mons_rand_name_draw]
    return mons_random_name_gen
    
mons_name = input("Please name the monster that you will be fighting against: ")
time.sleep(0.9)
click.clear()
loading_screen("Now spawning your very own monster")
time.sleep(2.3)
print("")
if mons_name != "":
	print(mons_name+"?","That's a pretty shitty name")
    print("")
	time.sleep(0.7)
	print("Well... whatever floats your boat..")
else:
    mons_random_name_gen()
    mons_name = mons_rand_name
    print("You will be fighting a randomly named monster. His name is",mons_rand_name)
time.sleep(4)
loading_screen("Loading")
#Difficulty Selection
#done
difficulty_setting = "x"
while difficulty_setting not in ("a","b","c"): 
	print("Please select your difficulty")
	print("")
	print("**  A = Easy  **")
	print("**  B = Normal  **")
	print("**  C = Difficult  **")
	print("")
	difficulty_setting = input("Type the first letter in front of your selected difficulty: ")
	difficulty_setting = difficulty_setting.lower()
	print (difficulty_setting)
	if difficulty_setting not in ("a","b","c"): 
		print("Difficulty not set, please try again")
		time.sleep(3)
		click.clear()
	else:
		print("")
#Difficulty Setting
#done
if difficulty_setting == "a":
	print("You're a chicken. Bawk bawk!")
    player_stats = {"max_hp":3000,"curr_hp":3000,"max_mp":2000,"curr_mp":2000,"evasion":30,"crit":30}
    player_status = {"regen":0,"mp_regen":0,"dot":0}
    mons_stats = {"max_hp":3000,"curr_hp":3000,"max_mp":2000,"curr_mp":2000,"evasion":10,"crit":10}
    mons_status = {"regen":0,"mp_regen":0,"dot":0}
elif difficulty_setting == "b":
	print("You're just the same as everyone, big deal.")
    player_stats = {"max_hp":3000,"curr_hp":3000,"max_mp":1500,"curr_mp":1500,"evasion":25,"crit":35}
    player_status = {"regen":0,"mp_regen":0,"dot":0}
    mons_stats = {"max_hp":4000,"curr_hp":4000,"max_mp":4000,"curr_mp":4000,"evasion":15,"crit":15}
    mons_status = {"regen":0,"mp_regen":0,"dot":0}
elif difficulty_setting == "c":
	print("Oh? So you think you're a big boy?")
    player_stats = {"max_hp":3000,"curr_hp":3000,"max_mp":1000,"curr_mp":1000,"evasion":20,"crit":40}
    player_status = {"regen":0,"mp_regen":0,"dot":0}
    mons_stats = {"max_hp":5000,"curr_hp":5000,"max_mp":5000,"curr_mp":5000,"evasion":20,"crit":20}
    mons_status = {"regen":0,"mp_regen":0,"dot":0}
else:
	print("Good job numbnuts, you broke something..")
	print("Are you too retarded to know what ABCs are?")
loading_screen("Setting Difficulty")  
click.clear()
print("Now that everything is ready, the battle will start shortly")
print("")
time.sleep(2)
input("Press enter to start fighting your own inner demons.")
click.clear()

##Functions: Battle Graphics
#def playericon():
#    return playericon
#def monsicon():
#    return monsicon
    

##Fuctions: Battle Status
#Player Health Bar
def player_hp(curr_hp,turn_dmg,max_hp):
    new_player_hp = curr_hp - turn_dmg
    global player_stats
    player_stats["curr_hp"] = int(new_player_hp)
    print("Player Health:",str(new_player_hp)+"/"+str(max_hp))
    return player_hp
#Monster Health Bar
def mons_hp(curr_hp,turn_dmg,max_hp):
    new_mons_hp = curr_hp - turn_dmg
    global mons_stats
    mons_stats["curr_hp"] = int(new_mons_hp)
    print("Monster Health:",str(new_mons_hp)+"/"+str(max_hp))
    return mons_hp
#Player Mana Bar
def player_mp(curr_mp,turn_mp_use,max_mp):
    new_player_mp = curr_hp - turn_dmg
    global player_stats
    player_stats["curr_mp"] = new_player_mp
    print("Player Mana:",str(new_player_mp)+"/"+str(max_mp))
    return player_mp
#Monster Mana Bar
def mons_mp(curr_hp,turn_mp_use,max_mp):
    new_mons_mp = curr_hp - turn_dmg
    global mons_stats
    mons_stats["curr_mp"] = new_mons_mp
    print("Monster Mana:",str(new_mons_mp)+"/"+str(max_mp))
    return mons_mp
#Player Poison Status
#Monster Burn Status

##Functions: Player Skills (Includes evasion and critical)
#Player Basic Attack Calc
def player_atk_dmg():
    global player_stats
    global mons_stats
    global player_atk
    player_atk_raw = random.randint(250,350)
    if random.randint(0,100) <= player_stats["crit"]:
        player_atk_crit = int(player_atk_raw * crit_multi)
    else:
        player_atk_crit = player_atk_raw
    if random.randint (0,100) <= mons_stat["evasion"]:
        player_atk_out = 0
    else:
        player_atk_out = player_atk_crit
    player_atk = player_atk_out
    return player_atk_dmg
#Player Heavy Attack Calc
def player_heavy_atk_dmg():
    global crit_multi
    global player_crit
    global mons_evasion
    global player_heavy_atk
    #delete above
    player_heavy_atk_raw = random.randint(380,460)
    if random.randint(0,100) <= player_crit:
        player_heavy_atk_crit = int(player_heavy_atk_raw * crit_multi)
    else:
        player_heavy_atk_crit = player_heavy_atk_raw
    if random.randint (0,100) <= mons_evasion:
        player_heavy_atk_out = 0
    else:
        player_heavy_atk_out = player_heavy_atk_crit
    player_heavy_atk = player_heavy_atk_out
    return player_heavy_atk_dmg
#Player Leech HP Calc
def player_leech_hp_dmg():
    global crit_multi
    global player_crit
    global mons_evasion
    global player_leech_hp
    #delete above
    player_leech_hp_raw = random.randint(150,200)
    if random.randint(0,100) <= player_crit:
        player_leech_hp_crit = int(player_leech_hp_raw * crit_multi)
    else:
        player_leech_hp_crit = player_leech_hp_raw
    if random.randint (0,100) <= mons_evasion:
        player_leech_hp_out = 0
    else:
        player_leech_hp_out = player_leech_hp_crit
    player_leech_hp = player_leech_hp_out
    return player_leech_hp_dmg
#Player Fireball Calc
def player_fireball_dmg():
    global crit_multi
    global player_crit
    global mons_evasion
    global player_fireball
    #delete above
    player_fireball_raw = random.randint(500,700)
    if random.randint(0,100) <= player_crit:
        player_fireball_crit = int(player_fireball_raw * crit_multi)
    else:
        player_fireball_crit = player_fireball_raw
    if random.randint (0,100) <= mons_evasion:
        player_fireball_out = 0
    else:
        player_fireball_out = player_fireball_crit
    player_fireball = player_fireball_out
    return player_fireball_dmg

#Functions: Monster Skills
#Monster Basic Attack Calc
def mons_atk_dmg():
    global crit_multi
    global mons_crit
    global player_evasion
    #delete above
    global mons_atk
    mons_atk_raw = random.randint(150,250)
    if random.randint(0,100) <= mons_crit:
        mons_atk_crit = int(mons_atk_raw * crit_multi)
    else:
        mons_atk_crit = mons_atk_raw
    if random.randint (0,100) <= player_evasion:
        mons_atk_out = 0
    else:
        mons_atk_out = mons_atk_crit
    mons_atk = mons_atk_out
    return mons_atk_dmg
#Monster Smash Calc
def mons_smash_dmg():
    global crit_multi
    global mons_crit
    global player_evasion
    global mons_smash
    #delete above
    mons_smash_raw = random.randint(400,800)
    if random.randint(0,100) <= mons_crit:
        mons_smash_crit = int(mons_smash_raw * crit_multi)
    else:
        mons_smash_crit = mons_smash_raw
    if random.randint (0,100) <= player_evasion:
        mons_smash_out = 0
    else:
        mons_smash_out = mons_smash_crit
    mons_smash = mons_smash_out
    return mons_smash_dmg
#Monster Poison Lick Calc
def mons_lick_poison_dmg():
    global crit_multi
    global mons_crit
    global player_evasion
    global mons_lick_poison
    #delete above 
    mons_lick_poison_raw = random.randint(50,100)
    if random.randint(0,100) <= mons_crit:
        mons_lick_poison_crit = int(mons_lick_poison_raw * crit_multi)
    else:
        mons_lick_poison_crit = mons_lick_poison_raw
    if random.randint (0,100) <= player_evasion:
        mons_lick_poison_out = 0
    else:
        mons_lick_poison_out = mons_lick_poison_crit
    mons_lick_poison = mons_lick_poison_out
    return mons_lick_poison_dmg

#Banter & Battle Messages
def mons_banter():
    global mons_name
    choice = random.randint(1,4)
    if choice == 1:
        print(mons_name,"is thinking of a way to fight back!")
    elif choice == 2:
        print("You have made",mons_name,"very angry, he will think of a revenge")
    elif choice == 3:
        print(mons_name,"wants to scold you but he has no mouth")
    else:
        print(mons_name+": I will destroy you!")
    return mons_banter
def player_banter():
    global player_name
    choice = random.randint(1,4)
    if choice == 1:
        print("")
    elif choice == 2:
        print("")
    elif choice == 3:
        print("")
    else:
        print("")
    return mons_banter
def player_atk_msg(atkdmg):
    global player_turn_atk
    global player_atk_name
    global player_name
    global mons_name
    choice = random.randint(1,2)
    if atkdmg == 0:
        if choice == 1:
            print(player_name,"tried to use",player_atk_name,"but missed!")
        else:
            print(player_name,"tried to use",player_atk_name,"but",mons_name,"managed to evade!")
    else:
        print(player_name,"used",player_atk_name,"and damaged",mons_name,"for",player_turn_atk,"damage!")
    return player_atk_msg
def mons_atk_msg(atkdmg):
    global mons_turn_atk
    global mons_atk_name
    global mons_name
    global player_name
    choice = random.randint(1,2)
    if atkdmg == 0:
        if choice == 1:
            print(mons_name,"tried to use",mons_atk_name,"but missed! (because he's a blind monster)")
        else:
            print(mons_name,"tried to use",mons_atk_name,"but",player_name,"was too fast!")
    else:
        print(mons_name,"used",mons_atk_name,"and damaged",player_name,"for",mons_turn_atk,"damage!")
    return mons_atk_msg

##Battle Logic
while player_curr_health > 0 or mons_curr_health > 0:
    player_turn_atk = 0
    mons_turn_atk = 0
    player_hp(player_curr_health,mons_turn_atk,player_max_health)
    mons_hp(mons_curr_health,player_turn_atk,mons_max_health)
    print("")
    print("")
    ##Player Turn
    print("Please select the move that you wish to use this turn.")
    print("1: Normal Attack")
    print("2: Heavy Attack")
    print("3: Leech HP")
    print("4: Fireball")
    player_atk_option = input("Please enter the attack number (1/2/3/4): ")
    if player_atk_option == "1":
        player_atk_dmg()
        player_turn_atk = player_atk
        player_atk_name = str("Normal Attack")
    elif player_atk_option == "2":
        player_heavy_atk_dmg()
        player_turn_atk = player_heavy_atk
        player_atk_name = str("Heavy Attack")
    elif player_atk_option == "3":
        player_leech_hp_dmg()
        player_turn_atk = player_leech_hp
        player_atk_name = str("Leech HP")
    elif player_atk_option == "4":
        player_fireball_dmg()
        player_turn_atk = player_fireball
        player_atk_name = str("Fireball")
    else:
        print(player_name,"is a retarded piece of wood.")
    print("")
    click.clear()
    player_hp(player_curr_health,mons_turn_atk,player_max_health)
    mons_hp(mons_curr_health,player_turn_atk,mons_max_health)
    print("")
    print("")
    player_atk_msg(player_turn_atk)
    print("")
    if mons_curr_health < 0:
        break
    input("Press enter to continue")
    print("It is now",mons_name,"turn to attack you. Be prepared")
    click.clear()
    player_turn_atk = 0
    mons_turn_atk = 0
    loading_screen("Monster turn coming up")
    click.clear()

    ## Monster Turn & AI Engine
    click.clear()
    player_turn_atk = 0
    mons_turn_atk = 0
    player_hp(player_curr_health,mons_turn_atk,player_max_health)
    mons_hp(mons_curr_health,player_turn_atk,mons_max_health)
    print("")
    print("")
    mons_banter()
    mons_think_time = random.randint(2,4)
    time.sleep(mons_think_time)
    monster_move_decision = random.randint(1,3)
    #1= Monster Basic Attack
    #2= Monster Smash Attack
    #3= Monster Lick Poison
    if monster_move_decision == 1:
        mons_atk_dmg()
        mons_turn_atk = mons_atk
        mons_atk_name = str("Basic Attack")
    elif monster_move_decision == 2:
        mons_smash_dmg()
        mons_turn_atk = mons_smash
        mons_atk_name = str("Smash")
    elif monster_move_decision == 3:
        mons_lick_poison_dmg()
        mons_turn_atk = mons_lick_poison
        mons_atk_name = str("Poison Lick")
    else:
        print("Monster is dumb, no moves this turn")
    click.clear()
    player_hp(player_curr_health,mons_turn_atk,player_max_health)
    mons_hp(mons_curr_health,player_turn_atk,mons_max_health)
    print("")
    print("")
    mons_atk_msg(mons_turn_atk)
    print("")
    if player_curr_health < 0:
        break
    input("Press enter to continue!")
    print("It is now your turn for revenge! Get ready.")
    player_turn_atk = 0
    mons_turn_atk = 0
    loading_screen("Your turn again")
    click.clear()
if mons_curr_health < 0:
	print("You have slain the monster!")
else:
	print("You have been slain!")
##Research for Text Wrapping https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/

##Research for disabling kb https://stackoverflow.com/questions/29289945/how-to-temporarily-disable-keyboard-input-using-python
