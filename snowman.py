# Snowman.py

import random
from ascii_art import STAGES


# List of secret words
def load_words():
    return ["python", "git", "github", "snowman", "meltdown"]

WORDS = load_words()

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """ Displays the stage of snowman melting,
    current blanks (_) and solved letters.
    """
    print(STAGES[mistakes]) # the more mistakes, the later stage is printed
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    """ Runs the display function and gets the next letter input from the user.
    """
    secret_word = get_random_word()
    unique_letters = set(secret_word)
    guessed_letters = []
    mistakes = 0
    MAX_MISTAKES = 3

    print("Welcome to Snowman Meltdown!")

    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        # Handle guess
        if guess in secret_word:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
        else:
            mistakes += 1

        # End conditions
        if len(guessed_letters) == len(unique_letters):
            print("You win!")
            break

        if mistakes > MAX_MISTAKES:
            print("You lose!")
            break        

        display_game_state(mistakes, secret_word, guessed_letters)


if __name__ == "__main__":
    play_game()