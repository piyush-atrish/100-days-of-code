# Day 3 - Treasure Island Adventure Game  
# Concepts learned:  
# - Multi-line strings (triple quotes ''' for ASCII art)  
# - User input handling with input().lower() for case-insensitive choices  
# - Conditional logic (if/elif/else) for branching story paths  
# - Program exit control using exit() to terminate early  
# - String manipulation and logical operators (and) for combined conditions  

# ASCII art for visual appeal (escape characters handled)
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print('Welcome to the Treasure Hunt!!!')

# First decision: Left or Right
n = input('You have two choices: go left or right. Choose! ').lower()
if n == 'right':
    print('You lost your way!!! Contact your mama ^^')
    exit()  # Terminates program if wrong choice
else:
    print('You have arrived at the shore.')

# Second decision: Swim or Wait
n = input('Do you want to swim or wait for a boat? (swim/wait) ').lower()
if n == 'swim':
    print('Oopsie! You are lunch for the sharks!! Bye!')
    exit()
else:
    print('The boat arrived.')

# Third decision: Share treasure? + Cave choice
n = input('The old man dropped you at Treasure Island.\nDo you want to share some treasure with him? (yes/no) ').lower()
m = input('You see three caves: red, blue, and green. Choose one! (r/g/b) ').lower()

# Nested logic for treasure outcome
if m == 'r' and n == 'no':
    print('You found the treasure!!')
    print("BUT the old man is the ruler of the island. You should've been nice!\nNo treasure for you.")
elif m == 'r' and n == 'yes':
    print('You found the treasure!!')
    print('The old man is the ruler. He rewards your kindness! Congratulations!!!')
elif m == 'g':
    print('You got eaten by bugs!!')
    exit()
elif m == 'b':
    print('You entered a volcanic cave. FIREEEEE!!!')
    exit()