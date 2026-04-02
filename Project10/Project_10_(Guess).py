# from random import randint
# EASY_LEVEL_TURNS  = 10
# HARD_LEVEL_TURNS  = 5
#
# print("Welcome to the Number Guessing Game !")
#
# def check_answer(user_guess, actual_answer,turns):
#     if user_guess > actual_answer:
#             print("Too High")
#             return turns-1
#     elif user_guess < actual_answer:
#             print("Too Low")
#             return turns-1
#     else:
#             print(f"You got it! The answer was {actual_answer}")
#             return None
#
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
#
# def game():
#     print("I am thinking of a Number between 1 & 100.")
#     answer = randint(1,100)
#     turns = set_difficulty()
#     guess = 0
#     while guess!= answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         guess = int(input("Make a guess: "))
#         turns = check_answer(guess,answer,turns)
#         if turns == 0:
#             print("You have run out of guesses, you loose")
#             return
#         elif guess!= answer:
#             print("Guess Again!")
# game()

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"🎉 You got it! The answer was {actual_answer}.")
        return None

def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = None

    while guess != answer:
        if turns == 0:
            print(f"You ran out of guesses. The correct number was {answer}.")
            break

        print(f"\nYou have {turns} attempt(s) remaining.")
        try:
            guess = int(input("Make a guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        turns = check_answer(guess, answer, turns)

        if turns != 0 and guess != answer:
            print("Guess again.")
game()


# def start_game():
#     while True:
#         game()
#         play_again = input("\nDo you want to play again? Type 'yes' or 'no': ").lower()
#         if play_again != "yes":
#             print("Thanks for playing. Goodbye!")
#             break
#         print("\n" + "-"*40 + "\n")
# start_game()