from colorama import init, Fore, Style

# Initialize colorama
init()
print(Fore.YELLOW+r'''
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
__________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************)
'''+ Style.RESET_ALL)

print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You are at the crossroad. Where do you want to go? Left, Right, or moving straight: ")
if direction == "right":
    print("You fell in the hole. Game over!")
elif direction == "left":
    decision = input("You arrive at a river. Do you want to 'wait' for a boat or 'swim' across? ")
    if decision == "swim":
        print("You Drowned. Game over!")
    elif decision == "wait":
        choose = input("Which colour gate do you want to pick? Blue, Red, or Yellow: ")
        if choose == "blue":
            print("You were eaten by beasts. Game over!")
        elif choose == "red":
            print("You were burned by fire. Game over!")
        elif choose == "yellow":
            print("You found the treasure. You win!")
        else:
            print("Invalid choice. Game over!")
    else:
        print("Invalid action. Game over!")
elif direction == "moving straight":
    print("You were hit by a truck. Game over!")
else:
    print("Invalid direction. Game over!")


# from colorama import init, Fore, Style
#
# # Initialize colorama
# init()
#
# # ASCII Art with color
# print(Fore.YELLOW + r'''
# ******************************************************************
# |                                                                |
# |               _.--"""""--._                                    |
# |             .'           '.                                   |
# |            /   O      O    \                                  |
# |           :           `    :                                  |
# |           |                |                                  |
# |           :    .------.    :                                  |
# |            \  '        '  /                                   |
# |             '.          .'                                    |
# |               '-......-'                                     |
# |                                                                |
# ******************************************************************
# ''' + Style.RESET_ALL)
#
# # Game intro with color
# print(Fore.CYAN + "Welcome to the Treasure Island.")
# print("Your mission is to find the treasure." + Style.RESET_ALL)
#
# # First decision
# direction = input(Fore.GREEN + "You are at the crossroad. Where do you want to go? Left, Right, or moving straight: " + Style.RESET_ALL).lower()
#
# if direction == "right":
#     print(Fore.RED + "You fell in the hole. Game over!" + Style.RESET_ALL)
# elif direction == "left":
#     decision = input(Fore.GREEN + "You arrive at a river. Do you want to 'wait' for a boat or 'swim' across? " + Style.RESET_ALL).lower()
#     if decision == "swim":
#         print(Fore.RED + "You Drowned. Game over!" + Style.RESET_ALL)
#     elif decision == "wait":
#         choose = input(Fore.GREEN + "Which colour gate do you want to pick? Blue, Red, or Yellow: " + Style.RESET_ALL).lower()
#         if choose == "blue":
#             print(Fore.RED + "You were eaten by beasts. Game over!" + Style.RESET_ALL)
#         elif choose == "red":
#             print(Fore.RED + "You were burned by fire. Game over!" + Style.RESET_ALL)
#         elif choose == "yellow":
#             print(Fore.MAGENTA + Style.BRIGHT + "🎉 You found the treasure. You win! 🎉" + Style.RESET_ALL)
#         else:
#             print(Fore.RED + "Invalid choice. Game over!" + Style.RESET_ALL)
#     else:
#         print(Fore.RED + "Invalid action. Game over!" + Style.RESET_ALL)
# elif direction == "moving straight":
#     print(Fore.RED + "You were hit by a truck. Game over!" + Style.RESET_ALL)
# else:
#     print(Fore.RED + "Invalid direction. Game over!" + Style.RESET_ALL)
