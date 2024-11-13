"""
Code written by Jackson L. Davis

This is the main Python file to run.
This program simulates a bingo game.
This program takes input using the input() function.
"""

from bingo_card import BingoCard
import random as rand

if __name__ == '__main__':
    print("Welcome to Bingo!")

    # set up number of players
    number_of_players = 0
    while number_of_players < 1 or number_of_players > 8:
        try:
            number_of_players = int(input("How many players? (1-8): "))
            if number_of_players < 1:
                print("You need at least 1 player.")
            elif number_of_players > 8:
                print("You cannot have more than 8 players.")
            else:
                pass
        except:
            print("You need to enter a number.")

    # set up player names and bingo cards
    bingo_cards = []
    for i in range(number_of_players):
        bingo_cards.append(BingoCard(input("Player " + str(i + 1) + " of " + str(number_of_players) + ", enter your name: ")))
    BingoCard.print_cards(bingo_cards)

    # set up type of bingo
    print("What do you want to count as a bingo?")
    print("(1) Any horizontal line")
    print("(2) Any vertical line")
    print("(3) Any line including horizontal, vertical, and diagonal lines")
    print("(4) Blackout")
    game_type = 0
    while game_type < 1 or game_type > 4:
        try:
            game_type = int(input("Select a type of bingo (1-4): "))
            if game_type < 1 or game_type > 4:
                print("You need to enter a number from 1 to 4.")
            else:
                pass
        except:
            print("You need to enter a number from 1 to 4.")

    # play bingo
    order_of_numbers = rand.sample(range(1, 76), 75)
    winners = []

    for number in order_of_numbers:
        user_input = input("Press enter to draw a number, or enter q to quit: ")
        if user_input == "q":
            break
        else:
            print("Number drawn: " + str(number))
            for card in bingo_cards:
                card.stamp_number(number)

                # check for bingos
                if game_type == 1:
                    if card.has_horizontal_line():
                        winners.append(card.name)
                    else:
                        pass
                elif game_type == 2:
                    if card.has_vertical_line():
                        winners.append(card.name)
                    else:
                        pass
                elif game_type == 3:
                    if card.has_line():
                        winners.append(card.name)
                    else:
                        pass
                else:
                    if card.has_blackout():
                        winners.append(card.name)
                    else:
                        pass

        # if there are any winners, stop the game after the turn is over
        BingoCard.print_cards(bingo_cards)
        if len(winners) > 0:
            break
        else:
            pass

    if len(winners) == 1:
        print("BINGO!")
        print(winners[0] + " wins!")
    elif len(winners) > 1:
        print("BINGO!")
        print("We have a tie! The co-winners are")
        for winner in winners:
            print(winner)
    else:
        print("Nobody wins.")
