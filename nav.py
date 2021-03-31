import csv
import random
import os
import os.path
from os import path


def nav():
    nav = []
    for y in range (1,11):
        for x in range (1,11):
            
            N = 1
            W = 1
            E = 1
            S = 1

            N = random.randint(0,1)
            if N == 0:
                pass
            else:
                E = random.randint(0,1)
                if E == 0:
                    pass
                else:
                    W = random.randint(0,1)
                    if W == 0:
                        pass
                    else:
                        S = random.randint(0,1)
            
            if x == 1:
                W = 0
            if x == 5:
                E = 0
            if y == 1:
                S = 0
            if y == 5:
                N = 0
            
            biomes = ["Forest", "Lava fields", "Meadow", "Cave", "River lands"]

            biome = biomes[random.randint(0,len(biomes)-1)]

            nav.append([x,y,N,W,E,S,biome])


    for i in range(1,len(nav)):
        if nav[i][0] == str(int(nav[i-1][0])+1) and nav[i][1] == nav[i-1][1]:
            nav[i][3] = nav[i-1][4]
        if nav[i][1] == str(int(nav[i-10][1])-1) and nav[i][0] == nav[i-10][0]:
            nav[i][5] = nav[i-10][2]
        
    with open('map.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(nav)
            
    return nav