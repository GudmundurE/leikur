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

    
