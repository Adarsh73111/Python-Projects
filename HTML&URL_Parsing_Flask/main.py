from flask import Flask
import random
import functools

app = Flask(__name__)

# Generate a random number between 0 and 9 when the server starts
TARGET_NUMBER = random.randint(0, 9)


# --- TOPIC 393: Use Python Decorators to Style HTML Tags ---
# We create custom decorators to wrap our text in HTML tags.
def make_bold(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        # We call the original function, get its text, and wrap it in <b> tags
        return f"<b>{function(*args, **kwargs)}</b>"

    return wrapper


def make_emphasis(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        return f"<em>{function(*args, **kwargs)}</em>"

    return wrapper


# --- TOPIC 394 & Exercise 23: Advanced Decorators with *args and **kwargs ---
# Why *args and **kwargs? So this decorator can be used on ANY function,
# even if that function takes arguments (like the 'check_guess' function below).
def log_game_activity(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"--> [GAME LOG]: Executing '{function.__name__}'.")
        if kwargs:
            print(f"--> [GAME LOG]: User provided URL variables: {kwargs}")

        # Pass any arguments down to the original function
        return function(*args, **kwargs)

    return wrapper


# --- TOPIC 392: Rendering HTML Elements with Flask ---
@app.route('/')
@make_bold
@make_emphasis
@log_game_activity
def home():
    # Because of our decorators, this text will be bolded and italicized!
    return "<h1>Guess a number between 0 and 9!</h1>" \
           "<p>Add your guess to the URL. For example: http://127.0.0.1:5000/5</p>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


# --- TOPIC 391 & 395: URL Paths, Parsing, and the Final Project ---
# The <int:guess> tells Flask to look for an integer in the URL and pass it
# to our function as a variable named 'guess'.
@app.route('/<int:guess>')
@log_game_activity
def check_guess(guess):
    # Here we are returning raw HTML strings with inline CSS styling
    if guess > TARGET_NUMBER:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guess < TARGET_NUMBER:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    # debug=True activates the Flask Debugger (Topic 391), which shows errors
    # directly in the browser if your code crashes.
    app.run(debug=True)