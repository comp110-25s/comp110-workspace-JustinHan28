"""Program that replicates the famous online game wordle which takes inputed word and compares it to a hidden word"""

__author__ = "730758899"

"""Determines whether a character is within a word and returns a True/False based on that"""


def contains_char(word: str, character: str) -> bool:
    assert len(character) == 1, f"len('{character}') is not 1"
    count = 0  # counter variable used to exit out of while loop after you reach the end of the word
    while count < len(
        word
    ):  # traverses through all indices of word and compares it to the character
        if word[count] == character:
            return True
        count = count + 1  # adds 1 to count to move on to the next index
    return False


"""Compares a guess string to a secret string and returns a string of emojies that represent generally how close the guess is to the secret based on the rules of wordle"""


def emojified(guess: str, secret: str) -> str:
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"
    count = 0
    result = ""
    while count < len(
        secret
    ):  # set to boolean that keeps while loop going as long as count is less than the length of secret in order to traverse through secret
        if guess[count] == secret[count]:
            result = result + GREEN_BOX
        elif contains_char(secret, guess[count]):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        count = count + 1
    return result


"""Prompts the user to input a N length string and keeps prompting them until they do"""


def input_guess(expected_length: int) -> str:
    word = input(f"Enter a {expected_length} character word: ")  #
    while len(word) != expected_length:
        word = input(f"That wasn't {expected_length} chars! Try again: ")
    return word


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    count = 0
    while count < 6:  # while loop that counts number of turns
        print(f"===Turn {count + 1}/6===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {count+1}/6 turns!")
            return  # makes sure that after the user wins, the function exits and doesn't continue to prompt the user to keep guessing or tell the user that they ran out of turns
        count = count + 1
    print(
        "X/6 - Sorry, try again tomorrow!"
    )  # if the function does not exit during the while loop, the user ran out of turns


if __name__ == "__main__":
    main(secret="codes")
