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
    # player name input
    print(pyfiglet.figlet_format("WELCOME TO\n BRILLIANT BLACKJACK"))
    time.sleep(1)
    while True:
        name = typingInput("\nWelcome! please enter your name:\n").capitalize()
        if (name != "Computer") and (name != ""):
            print("\n")
            typingPrint(f"Welcome {name}!\n")
            break

        elif name == "Computer":
            typingPrint("\nSorry you cannot be the computer! please enter a valid name!\n")
            print("\n")
        
        else: typingPrint("\nSorry you didnt input a name! please enter a valid name!\n")
        print("\n")
    # Game rules input
    while True:
        choices = typingInput("Would you like to read the rules of the game? (Type Y for yes and N for no):").lower()
        if choices == "y":
            typingPrint("I see.... you need a little help....here you go!")
            game_rules()
        elif choices == "n" :
            typingPrint("You like to live dangerously.... I like it! lets play!!!")
            start_game()
        else:
            typingPrint("Sorry you can only select Y for (yes) or N for (no), please try again")


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