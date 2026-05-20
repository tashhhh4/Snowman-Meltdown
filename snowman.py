# Snowman.py

from ascii_art import STAGES
from word_choice import WORDS
from game_logic import run_game
from console import get_y_n


if __name__ == "__main__":
    while True:
        run_game(STAGES, WORDS)
        if not get_y_n("Do you want to play again? (y/N) "):
            break