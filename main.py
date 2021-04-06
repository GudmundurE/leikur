import random
import classes
import mobs
import nav
import directions
import weapons
import fight
from playsound import playsound
from os import system

cls = lambda: system('cls')

playsound('Tonlist_Leikur_1.mp3', False)

kort = nav.nav()

x_pos = random.randint(4,8)
y_pos = random.randint(4,8)

player_xp = 0
cls()
print("Welcome")
wants_to_play = input("Press enter to start playing...")
cls()

while True:

       print("You play as a dwarf who is on his way to a bar")
       class_chosen = input("Chose your class: Warrior/1, Ranger/2, Mage/3: ")
       
       if class_chosen == "1":
              player_class = "Warrior"
              player_hp, player_dmg, player_luck = classes.Warrior()

              weapon_chosen = input("Choose your weapon: Axe/1, Sword/2: ")
              if weapon_chosen == "1":
                     dmg_mod, hit_chance = weapons.Axe()
                     player_dmg = float(player_dmg) * dmg_mod
                     int(round(player_dmg))
              elif weapon_chosen == "2":
                     dmg_mod, hit_chance = weapons.Sword()
                     player_dmg = float(player_dmg) * dmg_mod
                     int(round(player_dmg))
              break
       
       elif class_chosen == "2":
              player_class = "Ranger"
              player_hp, player_dmg, player_luck = classes.Ranger()

              weapon_chosen = input("Choose your weapon: Bow/1, Crossbow/2: ")
              if weapon_chosen == "1":
                     dmg_mod, hit_chance = weapons.Bow()
                     player_dmg = float(player_dmg) * dmg_mod
                     int(round(player_dmg))
              elif weapon_chosen == "2":
                     dmg_mod, hit_chance = weapons.Crossbow()      
                     player_dmg = float(player_dmg) * dmg_mod
                     int(round(player_dmg)) 
              
              break
              
       elif class_chosen == "3":
              player_class = "Mage"
              player_hp, player_dmg, player_luck = classes.Mage()

              weapon_chosen = input("Choose your weapon: Firestaff/1, Frostaff/2: ")
              if weapon_chosen == "1":
                     dmg_mod, hit_chance = weapons.Firestaff()
                     player_dmg = float(player_dmg) * dmg_mod
                     int(round(player_dmg))
              elif weapon_chosen == "2":
                     dmg_mod, hit_chance = weapons.Froststaff()
                     player_dmg = float(player_dmg) * dmg_mod
                     int(round(player_dmg))

              break
       else:
              class_chosen = input("Choose a class by selecting 1, 2 or 3: ") 



print("You start with", player_hp, "hp,", player_dmg, "dmg and", player_luck, "luck", hit_chance, dmg_mod)
input("Press enter to continue...")



while True:
       cls()
       print("You have", player_hp,"hp")
       print("You have",player_xp,"xp")
       for row in kort:
              if row[0] == x_pos and row[1] == y_pos:
                     N,W,E,S = int(row[2]),int(row[3]),int(row[4]),int(row[5])
                     biome = row[6]
                     print ("You have entered", biome) 
                     break
       
       x_pos,y_pos = directions.direct(N,W,E,S,x_pos,y_pos)
       
       event_chance = random.randint(1,100)


       fight_chance = random.randint(1,100)

       if fight_chance < 70:
              player_xp, player_hp = fight.fight_mob(player_luck,player_xp,player_dmg,player_hp,hit_chance,player_class, biome)