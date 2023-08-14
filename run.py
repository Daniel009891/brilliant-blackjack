import random
import pyfiglet
import time
import sys

suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def game_introduction():
    """
    Displays a welcome message for the user.
    Asks user to input a name.
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
            print(pyfiglet.figlet_format(f"Welcome {name}!\n"))
            break

        elif name == "Computer":
            typingPrint("\nSorry you cannot be the computer! "
                        "please enter a valid name!\n")
            print("\n")
        else:
            typingPrint("\nSorry you didn't input a name! "
                        "please enter a valid name!\n")
        print("\n")
    # Game rules input
    time.sleep(1)
    while True:
        print("\n")
        choices = typingInput("\nWould you like to read the rules of the game?"
                              "(Type Y for yes and N for no):").lower()
        if choices == "y":
            print("\n")
            typingPrint("I see.... you need a little help....here you go!")
            time.sleep(1)
            game_rules()
            

        elif choices == "n":
            print("\n")
            typingPrint("You like to live dangerously.... I "
                        "like it! lets play!!!")
            time.sleep(1)
            start_game()
            

        elif choices == "":
            typingPrint("Sorry you didnt make a selection. "
                        "Please type Y for yes or N for no")

        else:
            typingPrint("\nSorry you can only select "
                        "Y for (yes) or N for (no), "
                        "please try again!\n")
            print("\n")


def game_rules():
    """"
    Displays the rules of the game for the user if selected
    on the game introduction.
    """
    print(pyfiglet.figlet_format("\nBRILLIANT BLACKJACK RULES OF PLAY"))
    print("\n")
    typingPrint("""\n
The aim of brilliant blackjack is to score more point than the computer,
without scoring more than 21.

Point are awarded in conjunction to the number on the cards
dealt to both players.

Picture cards (Jack, Queen and king) are worth 10 points each.

Aces are high (11 points) or low (1 point) depending on the total score.

When the game starts, players are dealt 2 cards each from the shuffled
pack of cards. You will only 'see' one of the computer's cards.

If you have a score less than 21 points, you will have the option
to either STICK with the cards you have or TWIST and receive another card.

If you score 21 points with your first 2 cards, you score BLACKJACK and the 
game continues.

If you score more than 21 points, you will be BUST and the game continues.

The computer will choose to 'TWIST' or 'STICK' - which finishes the game
    """)
    options = typingInput("\nwould you like to start the game? "
                          "Please select Y to play or N to exit:\n").lower()
    if options == "n":
        typingPrint("\nSorry to see you go!!")
        print(pyfiglet.figlet_format("\nCome Back Soon"))
        sys.exit()
    elif options == "y":
        print(pyfiglet.figlet_format("\nGame On!"))
        start_game()
    elif options == "":
        typingPrint("\nSorry you didnt make a selection. "
                    "Please type Y to start game or N to exit")
    else:
        typingPrint("Sorry you can only select Y to play or N to exit")


def create_pack_of_cards():
    """
    Creates an ordered list (pack) as strings, converts
    list to dictionary pack of cards, to add card values to card keys
    converts dictionary back to a list (pack), shuffles the pack and 
    converts the shuffled list to shuffled dictionary.
    """
    pack = []
    for suit in suits:
        for card in cards:
            pack.append(card + "of" + suit)
    pack_of_cards = dict(zip(pack, values*4))
    pack = list(pack_of_cards.items())
    print("\n")
    typingPrint("Shuffling the deck.....\n")
    time.sleep(1)
    random.shuffle(pack)
    pack = dict(pack)
    return pack
    

def create_computer_cards(pack):
    print("computer hand created")


def start_game():
    """
    Starts the game and cycles through the associated
    functions before asking the player if they'd like 
    to play again.
    """
    pack = create_pack_of_cards()
    computer_cards = create_computer_cards(pack)
    


def typingPrint(text):
    """
    Not my code, taken from https://www.101computing.net/python-typing-text-effect/
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    """
    Not my code, taken from https://www.101computing.net/python-typing-text-effect/
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


game_introduction()
