import random

def skeleton():

    name = "a skeleton"
    hp = 80
    dmg = 7
    xp = 10

    return [name,hp,dmg,xp]

def zombie():

    name = "a zombie"
    hp = 130
    dmg = 7
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
'''
def cave_troll():

    name = "a cave troll"
    hp = 300
    dmg 12
    xp = 100    

    return [name,hp,dmg,xp]

def tree_man():

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
'''
def boss():

    name = "the BOSS"
    hp = 500
    dmg = 20
    xp = 1000

    return [name,hp,dmg,xp]

def generate_mob(player_luck, player_xp):
        #LAGA REIKNING, REIKNINGUR VERA MJÖG LÉLEGUR
        if player_xp < 100:
            chance = ((10+(random.uniform(13,18)*float(player_luck)))-float(player_xp))

            int(round(chance))

            if chance >= 40:
                return pig()
            elif chance <= 39 and chance >= 35:
                return spider()
            elif chance <= 34 and chance >= 29:
                return skeleton()
            else:
                return zombie()
        else:
            return boss()

    
