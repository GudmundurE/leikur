import random

def skeleton():

    name = "a skeleton"
    hp = 80
    dmg = 7
    xp = 10

    return [name,hp,dmg,xp]

def zombie():

    name = "a zombie"
    hp = 120
    dmg = 4
    xp = 14

    return [name,hp,dmg,xp]

def spider():

    name = "a spider"
    hp = 70
    dmg = 6
    xp = 10

    return [name,hp,dmg,xp]

def pig():

    name = "a pig"
    hp = 20
    dmg = 0
    xp = 3

    return [name,hp,dmg,xp]


def cave_troll():

    name = "a cave troll"
    hp = 300
    dmg = 12
    xp = 100    

    return [name,hp,dmg,xp]

def rooter():

    name = "a tree man"
    hp = 400
    dmg = 8
    xp = 75

    return [name,hp,dmg,xp]

def lava_monster():

    name = "a lava monster"
    hp = 200
    dmg = 15
    xp = 100

    return [name,hp,dmg,xp]

def goblin_warrior():

    name = "a goblin warrior"
    hp = 120
    dmg = 5
    xp = 12

    return [name,hp,dmg,xp]

def goblin_ranger():

    name = "a goblin ranger"
    hp = 80
    dmg = 8
    xp = 12

    return [name,hp,dmg,xp]

def goblin_mage():

    name = "a goblin mage"
    hp = 60
    dmg = 12
    xp = 12

    return [name,hp,dmg,xp]

def gnome():

    name = "a gnome"
    hp = 50
    dmg = 3
    xp = 10

    return [name,hp,dmg,xp]

def river_spirit():

    name = "a river spirit"
    hp = 90
    dmg = 5
    xp = 30

    return [name,hp,dmg,xp]

def river_warrior():

    name = "the a river warrior"
    hp = 120
    dmg = 7
    xp = 40

    return [name,hp,dmg,xp]

def troll():

    name = "a troll"
    hp = 200
    dmg = 10
    xp = 100

    return [name,hp,dmg,xp]

def magma_golem():

    name = "a magma golem"
    hp = 150
    dmg = 12
    xp = 75

    return [name,hp,dmg,xp]

def molten_zombie():

    name = "a molten_zombie"
    hp = 70
    dmg = 14
    xp = 75

    return [name,hp,dmg,xp]

def lava_blob():

    name = "a lava blob"
    hp = 25
    dmg = 2
    xp = 24

    return [name,hp,dmg,xp]

def big_lava_blob():

    name = "a big lava blob"
    hp = 50
    dmg = 4
    xp = 34

    return [name,hp,dmg,xp]

def wood_elf():

    name = "a wood elf"
    hp = 150
    dmg = 10
    xp = 75

    return [name,hp,dmg,xp]

def scarecrow():

    name = "a scarecrow"
    hp = 175
    dmg = 10
    xp = 100

    return [name,hp,dmg,xp]

def big_fish():

    name = "a big fish"
    hp = 100
    dmg = 5
    xp = 30

    return [name,hp,dmg,xp]

def angry_farmer():

    name = "angry farmer"
    hp = 100
    dmg = 5
    xp = 30

    return [name,hp,dmg,xp]

def spiderling():

    name = "a spiderling"
    hp = 30
    dmg = 3
    xp = 15

    return [name,hp,dmg,xp]

def rootling():

    name = "a rootling"
    hp = 40
    dmg = 2
    xp = 15

    return [name,hp,dmg,xp]

def guard_dog():

    name = "a guard dog"
    hp = 45
    dmg = 3
    xp = 15

    return [name,hp,dmg,xp]


def river_imp():

    name = "a river imp"
    hp = 30
    dmg = 4
    xp = 10

    return [name,hp,dmg,xp]
    
def boss():

    name = "THE BOSS"
    hp = 500
    dmg = 20
    xp = 10000

    return [name,hp,dmg,xp]

def generate_mob(player_luck, player_xp, biome):
        #LAGA REIKNING, REIKNINGUR VERA MJÖG LÉLEGUR
        if player_xp < 500:
            chance = (500 - random.randint(1,50)) - player_xp

            int(round(chance))
            
            if biome == "a Field":
                if chance > 400:
                    return pig()
                elif chance > 300 and chance <= 400:
                    return guard_dog()
                elif chance > 200 and chance <= 300:
                    return angry_farmer()
                elif chance > 100 <= 200:
                    return scarecrow()

            elif biome == "a Forrest":
                if chance > 400:
                    return rootling()
                elif chance > 300 and chance <= 400:
                    mob_chance = random.randint(1,3)
                    if mob_chance == 1:
                        return zombie()
                    elif mob_chance == 2:
                        return skeleton()
                    elif mob_chance == 3:
                        return gnome()
                elif chance > 200 and chance <= 300:
                    return wood_elf()
                elif chance > 100 <= 200:
                    return rooter()

            elif biome == "Lava fields":
                if chance > 400:
                    return lava_blob()
                elif chance > 300 and chance <= 400:
                    mob_chance = random.randint(1,3)
                    if mob_chance == 1:
                        return skeleton()
                    elif mob_chance == 2:
                        return zombie()
                    elif mob_chance == 3:
                        return big_lava_blob
                elif chance > 200 and chance <= 300:
                    mob_chance = random.randint(1,2)
                    if mob_chance == 1:
                        return magma_golem()
                    elif mob_chance == 2:
                        return molten_zombie()
                elif chance > 100 <= 200:
                    return lava_monster()
            
            elif biome == "a Cave":
                if chance > 400:
                    return spiderling()
                elif chance > 300 and chance <= 400:
                    mob_chance = random.randint(1,3)
                    if mob_chance == 1:
                        return goblin_warrior()
                    elif mob_chance == 2:
                        return goblin_ranger()
                    elif mob_chance == 3:
                        return goblin_mage()
                elif chance > 200 and chance <= 300:
                    return spider()
                elif chance > 100 <= 200:
                    return cave_troll()
            
            elif biome == "River lands":
                if chance > 400:
                    mob_chance = random.randint(1,2)
                    if mob_chance == 1:  
                        return river_imp()
                    elif mob_chance == 2:
                        return big_fish
                elif chance > 300 and chance <= 400:
                    mob_chance = random.randint(1,3)
                    if mob_chance == 1:
                        return river_spirit()
                    elif mob_chance == 2:
                        return skeleton()
                    elif mob_chance == 3:
                        return zombie()
                elif chance > 200 and chance <= 300:
                    return river_warrior()
                elif chance > 100 <= 200: 
                    return troll()

        else:
            return boss()

    
