# KU1102 PENGENALAN KOMPUTASI

# TUGAS BESAR I
# COMBAT SYSTEM RPG (TURN-BASED)

# Dosen : Dr. Aditya Purwa Santika, S.Si., M.Si.
# Fakultas : FMIPA
# Kelas : K-04

# KELOMPOK 7
# 16023004 - Kevin Lucius Hosea
# 16023034 - Ibrahim Radhi Yusaputra Bahar
# 16023059 - Amalia Ramadhani Adityas
# 16023139 - Brian Irsandi Lisander
# 16023184 - Tobias Adytia Pandu Dewanata
# 16023374 - Naila Natasya Akmalia

# KAMUS

# name : string
# hero_hp : integer
# hero_damage : integer
# hero_potions : integer
# potion_effect : integer
# hero_defense : integer
# weapon_buff : integer
# buffed_weapon : integer
# enemy_hp : integer
# enemy_damage : integer
# enemy_heal : integer
# action : proceduore
# action1 : string
# action2 : string
# action3 : string
# action4 : string
# act_list : matrix (array of integer)
# act : integer
# enemy_action : integer

# ALGORITMA

# Intro
# Random dialog
input("Once upon a time, you are walking through a wild forest [Press Enter]")
input("Sudennly, a fairy named Paimon poked you from the back [Press Enter]")
print("Paimon: Hello traveler, what's your name?")
name = input("Enter your name: ") # Input player's name
input(f"Paimon: Huh, what an interesting name, {name} [Press Enter]")
input("You: Umm.. okay?? [Press Enter]")
input("Paimon: Ehe, the thing is.. i saw a monster just a mile from here.. [Press Enter]")
input("Paimon: I'm scared the monster will hurt somebody.. would you please help me take care of it? [Press Enter]")
input("There's no other choice, you must help Paimon mwehehe [Press Enter]")
input("You prepared your gear, and after walking for a while, you found the monster. Off you go! [Press Enter]")
print()

# Stats Hero dan Monster

# Stats dasar player (Bisa di adjust)
hero_hp = 1500         # Base HP dari player
hero_damage = 150      # Base damage dari player
hero_potions = 4       # Jumlah potion yang dapat digunakan player 

# Stats dasar monster (Bisa di adjust)
enemy_hp = 4000        # Base HP dari monster     
enemy_damage = 150     # Base damage dari monster

# Deklarasi variabel (Jangan di adjust)
hero_defense = 0
weapon_buff = 0
buffed_weapon = hero_damage

# Deklarasi Procedure
def action(action1, action2, action3, action4):
    print("Choose an action: ")
    print(f"1. {(action1)}")
    print(f"2. {(action2)}")
    print(f"3. {(action3)}")
    print(f"4. {(action4)} ")
    print("Write the action number: ", end = "")

# Matrix 1 x 4 untuk pemanggilan action
act_list = [[1,2,3,4]]

# Proses Combat

# While loop agar combat terus berjalan selagi kedua karakter masih hidup (HP > 0)
while hero_hp > 0 and enemy_hp > 0:   
    print(f"Your Current HP: {hero_hp}")  # Display HP Player dan Monster yang tersisa di setiap round
    print(f"Monster's Current HP: {enemy_hp}")
    action("Attack", "Defend", "Forge Weapon", "Use Potion") # Penggunaan Procedure
    act = int(input()) # Input action

    print()
    
    # Kondisi yang terjadi berdasarkan action yang dipilih oleh pemain
    
    if act == act_list[0][0]:  # Action player = Attack
        enemy_hp -= hero_damage # Mekanisme attack
        print(f"[You hit the enemy for {hero_damage} damage!]")

    elif act == act_list[0][1]: # Action player = Defend
        hero_defense += 10 # Mekanisme Defend (Penambahan defense player) selagi belum mencapai batas maksimum
        if hero_defense <= 50: 
            print(f"[Decrease upcoming damage taken by 10%! Your current damage reduction is at {hero_defense}%!]")
        else: # Jika defense player melebihi batas maksimum (50) maka tidak terjadi apa-apa
            hero_defense = 50
            print(f"[Defense is at maximum ({hero_defense}% damage reduction)!]")

    elif act == act_list[0][2]: # Action player = Forge Weapon
        weapon_buff += 15   # Mekanisme Forge Weapon (damage buff player) selagi belum mencapai batas maksimum
        if weapon_buff <= 60: 
            hero_damage = ((buffed_weapon*(100 + weapon_buff))//100)
            print(f"[Your weapon damage is increased by 15%! Your current damage is increased by {weapon_buff}%]")
        else: # Jika damage buff player melebihi batas maksimum (60%) maka tidak terjadi apa-apa
            weapon_buff = 60
            print("[Your weapon is maxed out!]")

    elif act == act_list[0][3]: # Action player = Use Potion
        potion_effect = 250    # Kekuatan efek heal dari potion (Bisa di ajust)
        if hero_potions > 0:   # Mekanisme penggunaan potion, selagi potion masih tersisa
            hero_potions -= 1
            hero_hp += potion_effect
            print(f"[You used a potion! HP restored by {potion_effect}. You have {hero_potions} potion(s) remaining]")
        else:  # Jika potion habis maka tidak terjadi apa-apa
            print("[You ran out of potion!]")
    
    else: # Undefined action
        print("[Type carefully next time!]")
    
    # RNG 
    if enemy_hp > 0:
        enemy_action = 85053461164796801949539541639542805770666392330682673302530819774105141531698707146930307290253537320447270457 % enemy_hp
    # RNG memanfaatkan nilai sisa bagi dari suatu bilangan prima dengan sisa HP enemy
    # Jika nilai dari sisa pembagian ini ganjil, maka monster melakukan attack. Jika tidak, monster melakukan heal

    # Action yang dilakukan oleh monster berdasarkan RNG
    if enemy_action % 2 != 0: # Enemy action = Attack
        hero_hp = hero_hp - ((enemy_damage*(100 - hero_defense))//100) # Mekanisme attack dari monster yang damagenya dapat direduce berdasarkan defense player
        print(f"[Ouch! the monster hit you for {((enemy_damage*(100 - hero_defense))//100)} damage!]")

    else: # Enemy action = Heal
        enemy_heal = 200 # Kekuatan efek heal dari monster (Bisa di adjust)
        enemy_hp += enemy_heal # Mekanisme heal dari monster
        print(f"[The monster used heal! restoring {enemy_heal} HP]")

# Menentukan hasil combat ketika while loop mengalami break (terjadi ketika HP Player dan/atau HP Monster < 0)

# Hasil draw (Player dan Monster HP-nya < 0)
if hero_hp <= 0 and enemy_hp <= 0: 
    print()
    print("It's a draw! both of you died... Huh, how is that even possible?")
    print("GAME OVER")

# Player menang (HP player > 0 dan HP Monster < 0)
elif hero_hp > 0: 
    print() # Random dialog
    print("You have defeated the monster")
    input(f"Paimon: Yayy, you're so strong {name}, i knew i could count on you! [Press Enter]")
    input("You: Yeah.. it's kinda easy to be honest [Press Enter]")
    input("Paimon: Ugh, sure... [Paimon grabs something from her backpack] [Press Enter]")
    input('Paimon: As a gift, i will give you this "Blade Of Despair" [Press Enter]')      
    input("Paimon: This blade is extremely powerful.. use it with caution, it can shatter a mountain into two easily! [Press Enter]")
    input("You: Umm.. why would you give me something this great just because i defeated a weak monster? [Press Enter]")
    input("Paimon: I don't know, it's just heavy and i'm tired of carrying it, ehe [Press Enter]")
    print('After that, you come back to the city and sold the "Blade Of Despair" for a very high price and become super rich.')
    print("The End :D")   

# Player kalah (HP Player < 0 dan HP Monster > 0)
else: 
    print()
    print("The monster defeated you...")
    print("GAME OVER")
    
    

