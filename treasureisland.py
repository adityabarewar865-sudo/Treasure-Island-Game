print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island Game.")
print("Your mission is to find the treasure.")
choice1 = input("You are at crossroad, where do you want to go? type left or right:\n").lower()
if choice1 == "right":
    choice2 = input("You've come to a lake, there is a Island in the middle of the Sea. Type wait to wait for a boat, and swim to swim across:\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island safely. there is a house with three doors: red, yellow, blue. which colour do you choose?\n").lower()
        if choice3 == "red":
            print("Game Over! its a room full of fire.")
        elif choice3 == "yellow":
            print("HURRAY! YOU WON! YOU FOUND THE TREASURE!")
        elif choice3 == "blue":
            print("Game Over! its a room full of lions.")
        else:
            print("You entered a door that dosen't exist.")
    else:
        print("You got attacked by crocodiles.")
else:
    print("Game Over! you fell into a hole.")