# Snowman.py

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