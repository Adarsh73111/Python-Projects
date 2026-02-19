import random
stages = [
    '''
       +---+
       O   |
      /|\\  |
      / \\  |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
      /    |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
           |
          ===''',
    '''
       +---+
       O   |
      /|   |
           |
          ===''',
    '''
       +---+
       O   |
       |   |
           |
          ===''',
    '''
       +---+
       O   |
           |
           |
          ===''',
    '''
       +---+
           |
           |
           |
          ==='''
]
word_list = ["andaman and nicobar islands", "andhra pradesh", "arunachal pradesh", "assam", "bihar", "chandigarh", "chhattisgarh", "dadra and nagar haveli and daman and diu", "delhi", "goa", "gujarat", "haryana", "himachal pradesh", "jammu and kashmir", "jharkhand", "karnataka", "kerala", "ladakh", "lakshadweep", "madhya pradesh", "maharashtra", "manipur", "meghalaya", "mizoram", "nagaland", "odisha", "puducherry", "punjab", "rajasthan", "sikkim", "tamil nadu", "telangana", "tripura", "uttar pradesh", "uttarakhand", "west bengal"]
lives = 6
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display +=letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You Loose")
    if "_" not in display:
        game_over=True
        print("You win.")

    print(stages[lives])