# Snowman.py

from ascii_art import STAGES
from game_logic import run_game


# List of secret words
def load_words():
    return ["python", "git", "github", "snowman", "meltdown"]

WORDS = load_words()



if __name__ == "__main__":
    run_game(STAGES, WORDS)