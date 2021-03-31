import classes
import mobs
import nav

print("Welcome")
wants_to_play = input("Press 1 to start playing!: ")



while True:
       if wants_to_play == "1":
              print("Let's play!")

              print("You play as a dwarf who is on his way to a bar")
              class_chosen = input("Chose your class: Warrior/1, Ranger/2, Mage/3: ")
              
              if class_chosen == "1":
                     hp, dmg, luck = classes.Warrior()

                     weapon_chosen = input("Choose your weapon: Axe/1, Sword/2: ")
                     if weapon_chosen == "1":
                            dmg_mod, hit_chance = classes.Axe()
                     elif weapon_chosen == "2":
                            dmg_mod, hit_chance = classes.Sword()
                     break
              
              elif class_chosen == "2":
                     hp, dmg, luck = classes.Ranger()

                     weapon_chosen = input("Choose your weapon: Bow/1, Crossbow/2: ")
                     if weapon_chosen == "1":
                            dmg_mod, hit_chance, rel_time = classes.Bow()
                     elif weapon_chosen == "2":
                            dmg_mod, hit_chance, rel_time = classes.Crossbow()       
                     
                     break
                     
              elif class_chosen == "3":
                     hp, dmg, luck = classes.Mage()

                     weapon_chosen = input("Choose your weapon: Firestaff/1, Frostaff/2: ")
                     if weapon_chosen == "1":
                            dmg_mod, hit_chance = classes.Firestaff()
                     elif weapon_chosen == "2":
                            dmg_mod, hit_chance = classes.Froststaff()

                     break
              else:
                     class_chosen = input("Choose a class by selecting 1, 2 or 3: ")

              
                     
       else:   
              wants_to_play = input("Press 1 to start playing!: ")  



print("You start with ", hp, " hp, ", dmg, "dmg and ", luck, "luck", hit_chance, dmg_mod)



while left_or_right != "1" or "2":
              if left_or_right == "1":
                     print()
              elif left_or_right =="2":
                     print()
              else:
                     print("Choose 1 or")
       
