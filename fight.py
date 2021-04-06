import mobs
import random
import sys
from os import system

def fight_mob(player_luck,player_xp,player_dmg,player_hp,hit_chance,player_class,biome):
    
    cls = lambda: system('cls')
    cls()

    

    mob = mobs.generate_mob(player_luck,player_xp, biome)

    mob_health = int(mob[1])
    mob_dmg = int(mob[2])
    mob_xp = int(mob[3])

    print("You are faced with",mob[0], "it has, ", mob_health," hp")
    
    while mob_health > 0:
        chance = random.randint(1,100)
        chance += hit_chance
        if player_class == "Warrior":
            print("You can use:")
            print("1. Light Attack")
            print("2. Normal Attack")
            print("3. Heavy Attack")
            attack_type = input("Select your attack... ")
            cls()

            damage = random.randint(player_dmg,(player_dmg*player_luck))

            if attack_type == "1":
                if chance >= 33:
                    print("HIT!")
                    damage = float(damage) * 0.67
                    damage = int(round(damage))
                    mob_health -= damage
                    print("You did", damage, "damage!")
                    if mob_health > 0:
                        print("They have", mob_health,"hp left!")
                    else:
                        pass
                else:
                    print("You missed!!")
            elif attack_type == "2":
                if chance >= 50:
                    print("HIT!")
                    mob_health -= damage
                    print("You did", damage, "damage!")
                    if mob_health > 0:
                        print("They have", mob_health,"hp left!")
                    else:
                        pass
                else:
                    print("You missed!!")
            elif attack_type == "3":
                if chance >= 66:
                    print("HIT!")
                    damage = float(damage) * 1.33
                    damage = int(round(damage))
                    mob_health -= damage
                    print("You did", damage, "damage!")
                    if mob_health > 0:
                        print("They have", mob_health,"hp left!")
                    else:
                        pass
                else:
                    print("You missed!!")
        
        elif player_class == "Ranger":
            print("You can use:")
            print("1. Ranged Attack")
            print("2. Backstab")
            print("3. Stab")
            attack_type = input("Select your attack... ")
            cls()

            damage = random.randint(player_dmg,(player_dmg*player_luck))

            if attack_type == "1":
                if chance >= 20:
                    print("HIT!")
                    mob_health -= damage
                    print("You did", damage, "damage!")
                    if mob_health > 0:
                        print("They have", mob_health,"hp left!")
                    else:
                        pass
                else:
                    print("You missed!!")
            elif attack_type == "2":
                if chance >= 75:
                    print("HIT!")
                    damage = float(damage) * 3
                    damage = int(round(damage))
                    mob_health -= damage
                    print("You did", damage, "damage!")
                    if mob_health > 0:
                        print("They have", mob_health,"hp left!")
                    else:
                        pass
                else:
                    print("You missed!!")
            elif attack_type == "3":
                if chance >= 5:
                    print("HIT!")
                    damage = 15
                    mob_health -= damage
                    print("You did", damage, "damage!")
                    if mob_health > 0:
                        print("They have", mob_health,"hp left!")
                    else:
                        pass
                else:
                    print("You missed!!")

            
        elif player_class == "Mage":
            print("You can use:")
            print("1. Light Spell")
            print("2. Normal Spell")
            print("3. Heavy Spell")
            attack_type = input("Select your attack... ")
            cls()

            damage = random.randint(player_dmg,(player_dmg*player_luck))

            if attack_type == "1":
                if chance >= 33:
                    print("HIT!")
                    damage = float(damage) * 0.67
                    damage = int(round(damage))
                    mob_health -= damage
                    print("You did", damage, "damage!")
                    if mob_health > 0:
                        print("They have", mob_health,"hp left!")
                    else:
                        pass
                else:
                    print("You missed!!")
            elif attack_type == "2":
                if chance >= 50:
                    print("HIT!")
                    mob_health -= damage
                    print("You did", damage, "damage!")
                    if mob_health > 0:
                        print("They have", mob_health,"hp left!")
                    else:
                        pass
                else:
                    print("You missed!!")
            elif attack_type == "3":
                if chance >= 66:
                    print("HIT!")
                    damage = float(damage) * 1.33
                    damage = int(round(damage))
                    mob_health -= damage
                    print("You did", damage, "damage!")
                    if mob_health > 0:
                        print("They have", mob_health,"hp left!")
                    else:
                        pass
                else:
                    print("You missed!!")

        mob_hit = random.randint(1,100)

        if mob_health > 0:
            if mob_hit > 30:
                mob_dmg = random.uniform(1,2)*mob_dmg
                mob_dmg = int(round(mob_dmg))
                print("They did",mob_dmg,"damage!!")
                player_hp -= mob_dmg
                if player_hp <= 0:
                    print("They killed you!!")
                    print("Game over!")
                    input("Press enter to exit...")
                    sys.exit()
                print("You have",player_hp,"hp left!")
            else:
                print("They missed!")

    else:
        print("You killed it!")
        print("You gained",mob_xp,"xp!")
        player_xp += mob_xp
        input("Press enter to continue...")
        return player_xp, player_hp
        