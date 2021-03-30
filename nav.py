import csv
import random
import os
import os.path
from os import path


def nav():
    with open("map.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for y in range (1,6):
            for x in range (1,6):
                
                N = random.randint(0,1)
                E = random.randint(0,1)
                W = random.randint(0,1)
                S = random.randint(0,1)
                with open("map.csv", newline='') as file_read:
                    reader = csv.reader(file_read)
                    for row in reader:
                        if row[0] == str(x-1) and row[1] == str(y):
                            if row[4] == str(1):
                                W = 1
                                break
                            elif row[4] == str(0):
                                W = 0
                                break
                            else:
                                break
                        if row[1] == str(y-1) and row[0] == str(x):
                            if row[2] == str(1):
                                S = 1
                                break
                            elif row[2] == str(0):
                                S = 0
                                break
                            else:
                                break

                if x == 1:
                    W = 0
                if x == 5:
                    E = 0
                if y == 1:
                    S = 0
                if y == 5:
                    N = 0
                with open("map.csv", "a", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([x,y,N,W,E,S])

nav()


"""
def checkPos(x, y):
	N = 1
	W = 1
	E = 1
	S = 1

	if x == 1 and y == 1:
        N,W,E,S = 1,0,0,0
    if x == 2 and y == 1:
        N,W,E,S = 1,0,1,0
    if x == 3 and y == 1:
        N,W,E,S = 1,1,1,0
    if x == 4 and y == 1:
        N,W,E,S = 1,1,1,0
    if x == 5 and y == 1:
        N,W,E,S = 1,1,0,0
    if x == 1 and y == 2:
        N,W,E,S = 0,0,1,1
    if x == 2 and y == 2:
        N,W,E,S = 1,1,0,1
    if x == 3 and y == 2:
        N,W,E,S = 0,0,0,1
    if x == 4 and y == 2
        N,W,E,S = 0,0,1,1
    if x == 5 and y == 2:
        N,W,E,S = 1,1,0,1
    if x == 1 and y == 3:
        N,W,E,S = 1,0,1,0
    if x == 2 and y == 3:
        N,W,E,S = 1,1,1,1
    if x == 3 and y == 3:
        N,W,E,S = 1,1,1,0
    if x == 4 and y == 3:
        N,W,E,S = 1,1,0,0
    if x == 5 and y == 3:
        N,W,E,S = 1,0,0,1
    if x == 1 and y == 4:
        N,W,E,S = 1,0,0,1
    if x == 2 and y == 4:
        N,W,E,S = 0,0,0,1
    if x == 3 and y == 4:
        N,W,E,S = 1,0,1,1
    if x == 4 and y == 4:
        N,W,E,S = 1,1,0,1
    if x == 5 and y == 4:
        N,W,E,S = 1,0,0,1
    if x == 1 and y == 5:
        N,W,E,S = 0,0,1,1
    if x == 2 and y == 5:
        N,W,E,S = 0,1,1,0
    if x == 3 and y == 5:
        N,W,E,S = 0,1,1,1
    if x == 4 and y == 5:
        N,W,E,S = 0,1,1,1
    if x == 5 and y == 5:
        N,W,E,S = 0,1,0,1
	return N,W,E,S

def travelNorth(x, y):
	if y == 3:
		print("Not a valid direction!")
		return x,y
	elif x == 2 and y == 2:
		print("Not a valid direction!")
		return x,y
	else:
		y += 1
		return x,y

def travelEast(x, y):
	if x == 3:
		print("Not a valid direction!")
		return x,y
	elif x == 2 and y != 3:
		print("Not a valid direction!")
		return x,y
	else:
		x += 1
		return x,y

def travelWest(x, y):
	if x == 1:
		print("Not a valid direction!")
		return x,y
	elif x == 2 and y == 1:
		print("Not a valid direction!")
		return x,y
	elif x == 3 and y != 3:
		print("Not a valid direction!")
		return x,y	
	else:
		x -= 1
		return x,y

def travelSouth(x, y):
	if y == 1:
		print("Not a valid direction!")
		return x,y
	elif x == 2 and y == 3:
		print("Not a valid direction!")
		return x,y	
	else:
		y -= 1
		return x,y

N = 0
S = 0
W = 0
E = 0

current_y_pos = 1
current_x_pos = 1
last_x_pos = 0
last_y_pos = 0

halda_afram = True
while halda_afram:
	if current_x_pos == 3 and current_y_pos == 1:
		print("Victory!")
		halda_afram = False
	else:
		N,W,E,S = checkPos(current_x_pos, current_y_pos)
		

		if last_x_pos == current_x_pos and last_y_pos == current_y_pos:
			pass
		else:
			if N == 1 and S == 1 and W == 1:
				print("You can travel: (N)orth or (W)est or (S)outh.")
			elif N == 1 and S == 1 and E == 1:
				print("You can travel: (N)orth or (E)ast or (S)outh.")
			elif S == 1 and W == 1 and E == 1:
				print("You can travel: (E)ast or (W)est or (S)outh.")
			elif N == 1 and S == 1:
				print("You can travel: (N)orth or (S)outh.")
			elif N == 1 and W == 1:
				print("You can travel: (N)orth or (W)est.")
			elif N == 1 and E == 1:
				print("You can travel: (N)orth or (E)ast.")
			elif E == 1 and W == 1:
				print("You can travel: (E)ast or (W)est.")
			elif S == 1 and E == 1:
				print("You can travel: (E)ast or (S)outh.")
			elif S == 1 and W == 1:
				print("You can travel: (S)outh or (W)est.")
			elif N == 1:
				print("You can travel: (N)orth.")
			last_x_pos = current_x_pos
			last_y_pos = current_y_pos


		direct = input("Direction: ")
		
		if direct.lower() == "n":
			current_x_pos, current_y_pos = travelNorth(current_x_pos, current_y_pos)

		elif direct.lower() == "s":
			current_x_pos, current_y_pos = travelSouth(current_x_pos, current_y_pos)

		elif direct.lower() == "e":
			current_x_pos, current_y_pos = travelEast(current_x_pos, current_y_pos)

		elif direct.lower() == "w":
			current_x_pos, current_y_pos = travelWest(current_x_pos, current_y_pos)
"""
	
		



