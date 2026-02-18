import random
rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock
'''
paper = r'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
Paper
'''
scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors
'''
list_of_choices = [rock, paper, scissors]
print("Welcome to the Rock-Paper-Scissors Game!")
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))
if choose < 0 or choose > 2:
    print("Invalid choice. Please enter 0, 1, or 2.")
else:
    print("\nYou chose:")
    print(list_of_choices[choose])
    comp_choose = random.randint(0, 2)
    print("Computer chose:")
    print(list_of_choices[comp_choose])
    if choose == comp_choose:
        print("It's a draw!")
    elif (choose == 0 and comp_choose == 2) or \
         (choose == 1 and comp_choose == 0) or \
         (choose == 2 and comp_choose == 1):
        print("You win!")
    else:
        print("Computer wins!")
