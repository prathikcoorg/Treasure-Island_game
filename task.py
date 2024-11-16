print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('you\'re at a cross road where do you want to go?\n type "left" or "right".').lower()

if choice1 =="right":
    print("fall into a hole game over")

elif choice1 =="left":
     choice2=input('you safely came to the lake would you like to "swim" or "wait" or "jump"?').lower()

     if choice2 == "swim":
        print("attacked by trout game over!")

     elif choice2 =="jump":
         print("you drown to the water died game over")

     elif choice2=="wait":
         door=input("which door ? red or blue or yellow").lower()

         if door =="blue":
             print("eaten by a beast game over")

         elif door =="red":
             print("burned by fire game over")

         elif door =="yellow":
             choice3=input('you got two box to choose  key to open island! "box1" or "box 2"')
             if choice3 =="box1":
                 print("you got a key and win the game")
             else:
                 print("bomb blasted game over")

         else:
             print("game over")



