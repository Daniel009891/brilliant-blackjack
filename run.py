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
    If name is valid, function will call the game
    rules options function.
    """
    # player name input
    print(pyfiglet.figlet_format("WELCOME TO\n BRILLIANT BLACKJACK"))
    time.sleep(1)
    name = typingInput("\nWelcome! please enter your name:\n").capitalize()
    if (name != "Computer") and (name != ""):
        print("\n")
        print(pyfiglet.figlet_format(f"Welcome {name}!\n"))
        game_rules_options()

    elif name == "Computer":
        typingPrint("\nSorry you cannot be the computer! "
                    "please enter a valid name!\n")
        print("\n")
        game_introduction()
    else:
        typingPrint("\nSorry you didn't input a name! "
                    "please enter a valid name!\n")
        game_introduction()
    print("\n")


def game_rules_options():
    """
    Gives the user the option to read the rules
    or play the game without.
    """

    choices = typingInput("\nWould you like to read the rules of the game?"
                          "(Type Y for yes and N for no):\n").lower()
    if choices == "y":
        print("\n")
        typingPrint("I see.... you need a little help....here you go!")
        time.sleep(1)
        game_rules()
    elif choices == "n":
        print("\n")
        typingPrint("You like to live dangerously.... I "
                    "like it! lets play!!!")
        print(pyfiglet.figlet_format("\nGame On!"))
        time.sleep(1)
        start_game()    
    else:
        typingPrint("\nSorry you can only select "
                    "Y for (yes) or N for (no), "
                    "please try again!\n")
        print("\n")
        game_rules_options()


def game_rules():
    """"
    Displays the rules of the game for the user if selected
    on the game rules options function.
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
                          "Please select Y to play or No"
                          "to exit:\n").lower()
    if options == "n":
        typingPrint("\nSorry to see you go!!")
        print(pyfiglet.figlet_format("\nCome Back Soon"))
        sys.exit()
    elif options == "y":
        print(pyfiglet.figlet_format("\nGame On!"))
        start_game()

    else:
        typingPrint("Sorry you can only select Y to play or N to exit")
        game_rules_options()


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
    """
    Selects 2 cards for the computer from the shuffled
    pack and adds these to a new list.
    prints the first card, converts list to
    dictionary and sums values to get score
    """
    computer_cards = []
    while len(computer_cards) < 2:
        computer_cards.append(pack.popitem())
        typingPrint("Dealing the computers cards....")
        time.sleep(1)
        typingPrint("The computers first card is: ")
        print("\n")
        print(f"{computer_cards[0][0]}")
        time.sleep(1)
        computer_cards = dict(computer_cards)
        return computer_cards


def create_player_cards(pack):
    """
    Removes 2 cards for the player from the shuffled
    dictionary, adds them to a new list and converts
    new list to dictionary. Displays total score of hand
    to player.
    """
    player_cards = []
    while len(player_cards) < 2:
        player_cards.append(pack.popitem())
    player_cards = dict(player_cards)
    player_score = sum(player_cards.values())
    player_score = player_ace_values(player_cards)
    typingPrint("Your cards are: ")
    time.sleep(1)
    print("\n")
    for keys, value in player_cards.items():
        print(keys)
    time.sleep(1)
    your_score = ("Your score is: "
                  f"{player_score}")
    typingPrint(f"{your_score}")
    return player_cards


def player_ace_values(player_cards):
    """
    Analizes the players cards for aces if score is
    greater than 21 and changes one ace value from
    high(11) to low(1) whilever the score remains
    higher than 21.
    """
    player_score = sum(player_cards.values())
    if player_score > 21:
        for key, value in player_cards.items():
            if "Ace" in key and value == 11:
                updated_value = {key: 1}
                player_cards.update(updated_value)
                update_score = sum(player_cards.values())
                if update_score > 21:
                    continue
                else:
                    player_score = update_score
                    break
    return player_score


def computer_ace_values(computer_cards):
    """
    Analizes the computers cards for aces if score is
    greater than 21 and changes one ace value from
    high(11) to low(1) whilever the score remains
    higher than 21.
    """
    computer_score = sum(computer_cards.values())
    if computer_score > 21:
        for key, value in computer_score.items():
            if "Ace" in key and value == 11:
                updated_value = {key: 1}
                computer_score.update(updated_value)
                update_score = sum(computer_cards.values())
                if update_score > 21:
                    continue
                else:
                    computer_score = update_score
                    break
    return computer_score


def player_stick_twist_choice(pack, player_cards):
    """
    Displays a messgae to the user asking if they'd like
    to stick with their cards or twist and receive
    another card.
    """
    player_score = player_ace_values(player_cards)
    if player_score == 21:
        time.sleep(1)
        print(pyfiglet.figlet_format("***BLACKJACK***"))
        return player_score
    else:
        while player_score < 21:
            stick_twist = typingInput("\nWould you like to risk it all "
                                      "and twist? or chicken out and stick? "
                                      "Please select S for stick "
                                      "or T for twist: ").lower()
            
            if stick_twist == "t":
                time.sleep(1)
                typingPrint("You chose to be brave! excellent!")
                player_cards = twist(pack, player_cards)
                player_score = sum(player_cards.values())
                continue
            elif stick_twist == "s":
                time.sleep(1)
                typingPrint("You chose to chicken out! BOOOO!!")
                you_chose = (f"You chose to stick with"
                             f"{player_score} points")

                print(you_chose)
                return player_score
                break
            else:
                typingPrint("Sorry you can only chose to"
                            "Stick (S) or Twist (T)")
                continue
        return player_score


def twist(pack, player_cards):
    """
    Gives the player a new card from the deck and adds
    it to the players score.
    """
    player_cards_list = list(player_cards.items())
    time.sleep(1)
    typingPrint("Dealing you your new card....")
    player_cards_list.append(pack.popitem())
    time.sleep(1)
    new_card = (f"Your new card is the {player_cards_list[-1][0]}")
    


def start_game():
    """
    Starts the game and cycles through the associated
    functions before asking the player if they'd like
    to play again.
    """
    pack = create_pack_of_cards()
    computer_cards = create_computer_cards(pack)
    player_cards = create_player_cards(pack)
    player_score = player_stick_twist_choice(pack, player_cards)


def typingPrint(text):
    """
    Gives the typing effect to print statements,
    code has been taken from open source and
    credited within the README.md
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    """
    Gives the typing effect to inputs,
    code has been taken from open source and
    credited within the README.md
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


game_introduction()
