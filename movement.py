import classes
import mobs
import nav

kort = nav.nav()

x_pos = 0
y_pos = 0

for row in kort:
       if row[0] == x_pos and row[1] == y_pos:
              N,W,E,S = row[2],row[3],row[4],row[5]