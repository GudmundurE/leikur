def direct(N,W,E,S,x_pos,y_pos):
    while True:
        if N == 1 and W == 1 and E == 1 and S == 1:
            direction = input("You can move: (N)orth, (W)est, (E)ast or (S)outh: ")
            pass
        elif N == 1 and W == 1 and E == 1 and S == 0:
            direction = input("You can move: (N)orth, (W)est or (E)ast: ")
            pass
        elif N == 1 and W == 1 and E == 0 and S == 1:
            direction = input("You can move: (N)orth, (W)est or (S)outh: ")
            pass        
        elif N == 1 and W == 0 and E == 1 and S == 1:
            direction = input("You can move: (N)orth, (E)ast or (S)outh: ")
            pass
        elif N == 0 and W == 1 and E == 1 and S == 1:
            direction = input("You can move: (W)est, (E)ast or (S)outh: ")
            pass
        elif N == 1 and W == 1 and E == 0 and S == 0:
            direction = input("You can move: (N)orth or (W)est: ")
            pass
        elif N == 0 and W == 1 and E == 1 and S == 0:
            direction = input("You can move: (E)ast or (W)est: ")        
            pass
        elif N == 1 and W == 0 and E == 0 and S == 1:
            direction = input("You can move: (N)orth or (S)outh: ")
            pass
        elif N == 1 and W == 0 and E == 1 and S == 0:
            direction = input("You can move: (N)orth or (E)ast: ")
            pass
        elif N == 0 and W == 1 and E == 0 and S == 1:
            direction = input("You can move: (W)est or (S)outh: ")
            pass
        elif N == 0 and W == 0 and E == 1 and S == 1:
            direction = input("You can move: (E)ast or (S)outh: ")
            pass
        elif N == 1 and W == 0 and E == 0 and S == 0:
            direction = input("You can move: (N)orth: ")        
            pass
        elif N == 0 and W == 1 and E == 0 and S == 0:
            direction = input("You can move: (W)est: ")
            pass
        elif N == 0 and W == 0 and E == 1 and S == 0:
            direction = input("You can move: (E)ast: ")
            pass
        elif N == 1 and W == 0 and E == 0 and S == 1:
            direction = input("You can move: (S)outh: ")
            pass

        if direction == "N" and N == 1:
            y_pos += 1
        elif direction == "W" and W == 1:
            x_pos -= 1
        elif direction == "E" and E == 1:
            x_pos += 1
        elif direction == "S" and S == 1:
            y_pos -= 1
        elif direction == "n" and N == 1:
            y_pos += 1
        elif direction == "w" and W == 1:
            x_pos -= 1
        elif direction == "e" and E == 1:
            x_pos += 1
        elif direction == "s" and S == 1:
            y_pos -= 1
        else:
            print("Invalid input!...")
        
        return x_pos,y_pos