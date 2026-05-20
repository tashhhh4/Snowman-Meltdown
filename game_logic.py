import random
from console import get_single_letter


def get_random_word(words):
    """Selects a random word from the list."""
    return words[random.randint(0, len(words) - 1)]


def display_game_state(stages, mistakes, secret_word, guessed_letters):
    """ Displays the stage of snowman melting,
    current blanks (_) and solved letters.
    """
    print(stages[mistakes]) # the more mistakes, the later stage is printed
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def run_game(snowman_stages, word_list):
    """ Runs the display function and gets the next letter input from the user.
        snowman_stages: A list which defines the game by providing ASCII art at every element,
                        and setting the length of the game by the number of its elements.
        word_list: A list of words which can be chosen at random for the game.
    """
    secret_word = get_random_word(word_list)
    unique_letters = set(secret_word)
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(snowman_stages) - 1

    print("Welcome to Snowman Meltdown!")

    display_game_state(snowman_stages, mistakes, secret_word, guessed_letters)

    while True:
        guess = get_single_letter("Guess a letter: ")
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

        if mistakes > max_mistakes:
            print("You lose!")
            break        

        display_game_state(snowman_stages, mistakes, secret_word, guessed_letters)
