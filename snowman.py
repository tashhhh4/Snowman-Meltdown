# Snowman.py

from ascii_art import STAGES
from word_choice import WORDS
from game_logic import run_game


if __name__ == "__main__":
    run_game(STAGES, WORDS)