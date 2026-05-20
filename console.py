def get_single_letter(prompt):
    """ Prompts the user until a valid single letter is entered. """
    
    ERROR_TEXT = "Guess must be a single letter!"
    while True:
        user_input = input(prompt).lower().strip()
        
        if not user_input.isalpha():
            print(ERROR_TEXT)
            continue
        if not len(user_input) == 1:
            print(ERROR_TEXT)
            continue

        return user_input


def get_y_n(prompt):
    """ Gets the answer to a yes or no question. """
    user_input = input(prompt)
    if user_input.lower() in ["y", "yes"]:
        return True
    return False


def get_choice(prompt, choices):
    """ Displays a list of choices, numbered.
    Prompts the user to input a number value,
    and returns the choice as a string value
    prompt: str
    choices: [str]
    """
    for i, choice in enumerate(choices):
        print(f"{i + 1}: {choice}")
    while True:
        try:
            user_input = int(input(prompt))
            return choices[user_input - 1]
        except ValueError:
            print("Invalid input, try again.")
        except IndexError:
            print("Invalid input, try again.")