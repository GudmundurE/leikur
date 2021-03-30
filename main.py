import classes

print("Welcome")
wants_to_play = input("Press 1 to start playing!: ")

while True:
       if wants_to_play == "1":
              print("Let's play!")

              print("You play as a dwarf who is on his way to a bar")
              class_chosen = input("Chose your class: Warrior/1, Ranger/2, Mage/3: ")
              
              if class_chosen == "1":
                     hp, dmg, luck = classes.Warrior()
                     break
              
              elif class_chosen == "2":
                     hp, dmg, luck = classes.Ranger()
                     break
                     
              elif class_chosen == "3":
                     hp, dmg, luck = classes.Mage()
                     break
              else:
                     class_chosen = input("Choose a class by selecting 1, 2 or 3: ")
                     
       else:   
              wants_to_play = input("Press 1 to start playing!: ")  

print("You start with ", hp, " hp, ", dmg, "dmg and ", luck, "luck")
left_or_right = input("First choice... Left or Right (Left = 1 / Right = 2)?")
while left_or_right != "1" or "2":
              if left_or_right == "1":
                     print()
              elif left_or_right =="2":
                     print()
              else:
                     print("Choose 1 or")
       
