from Project11.game_data_prj11 import data
import random

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    account_platform = account["platform"]
    return f"{account_name}, a {account_description}, from {account_country}, present on platform {account_platform}."

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}")
    print("vs")
    print(f"Against B:{format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"*6)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right!, Current score {score}.")
    else:
        print(f"Sorry, that is wrong. Final score: {score}.")
        game_should_continue = False