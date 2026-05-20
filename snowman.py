""" ☃️ snowman.py ☃️

This is a game that can be played on the command line.

If you know Hangman, you already know how this works. For the
uninitiated, you will have to guess a word one letter at a time.

But don't take too long -- Your friend, SNOWMAN, is melting!

SNOWMAN needs YOU to guess the word, and fast! The word is the
secret password to the air-conditioning unit. Only by correctly
uncovering this secret word can you adjust the temperature of the
room, and save your frosty friend.

To play the game:

    python snowman.py
    
"""

from word_choice import WORDS
from game_logic import print_game_title, choose_difficulty, run_game
from console import get_y_n


if __name__ == "__main__":
    while True:
        print_game_title()
        stages = choose_difficulty()
        run_game(stages, WORDS)
        if not get_y_n("Do you want to play again? (y/N) "):
            break
