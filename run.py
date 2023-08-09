import random
import pyfiglet
import time
import sys


def game_introduction():
    """
    Displays a welcome message for the user.
    Asks if the user would like to read game instructions
    or play game.
    """
    print(pyfiglet.figlet_format("WELCOME TO\n BRILLIANT BLACKJACK"))
    time.sleep(1)

    name = typingInput("Welcome! please enter your name:")


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


game_introduction()