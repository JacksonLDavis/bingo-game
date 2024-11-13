"""
Code written by Jackson L. Davis

This class is for a 5x5 bingo card.
A bingo card will look something like this:
+--+--+--+--+--+
|07|22|41|58|67|
+--+--+--+--+--+
|14|18|36|49|74|
+--+--+--+--+--+
|03|19|  |52|71|
+--+--+--+--+--+
|10|28|35|55|73|
+--+--+--+--+--+
|08|16|40|50|66|
+--+--+--+--+--+
The first column contains five random numbers from 1-15
The second column contains five random numbers from 16-30
The third column contains four random numbers from 31-45 (the middle space is free)
The fourth column contains five random numbers from 46-60
The fifth column contains five random numbers from 61-75

When a randomly selected number is on the card,
the number on the card will be "stamped out" and disappear.
"""

import random as rand


class BingoCard:

    def __init__(self, name):
        """
        Constructor for the BingoCard
        :param name: a string representing a player's name 
        """
        self.__name = name
        self.__card = [[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]]

        # generate non-repeating random numbers
        b_col = rand.sample(range(1, 16), 5)
        i_col = rand.sample(range(16, 31), 5)
        n_col = rand.sample(range(31, 46), 5)
        g_col = rand.sample(range(46, 61), 5)
        o_col = rand.sample(range(61, 76), 5)

        # put numbers on bingo card
        for i in range(5):
            self.__card[i][0] = b_col[i]
            self.__card[i][1] = i_col[i]
            self.__card[i][2] = n_col[i]
            self.__card[i][3] = g_col[i]
            self.__card[i][4] = o_col[i]

        # remove middle space,
        # 0 will be used as a stamped space
        self.__card[2][2] = 0

    @property
    def name(self):
        """
        Getter method for the BingoCard name
        :return: a string of the name
        """
        return self.__name

    @property
    def card(self):
        """
        Getter method for the BingoCard card
        :return: a list of lists containing the numbers on the BingoCard
        """
        return self.__card

    def stamp_number(self, num):
        """
        Stamp out the given number if it is on the BingoCard
        :param num: a number to try to stamp out
        :postcond: if num is on the BingoCard, the number on the BingoCard turns into a 0 (stamped)
        """
        if num <= 15:
            column_to_check = 0
        elif num <= 30:
            column_to_check = 1
        elif num <= 45:
            column_to_check = 2
        elif num <= 60:
            column_to_check = 3
        else:
            column_to_check = 4
        for i in range(5):
            if self.__card[i][column_to_check] == num:
                # stamp out number
                self.__card[i][column_to_check] = 0
                return
            else:
                pass
        return

    def has_horizontal_line(self):
        """
        Determine if a BingoCard has a horizontal line stamped out
        :return: true if a horizontal line is stamped out, false otherwise
        """
        # check row
        for i in range(5):
            has_row = True
            # check row entries
            for j in range(5):
                if self.__card[i][j] != 0:
                    has_row = False
                    break
                else:
                    pass
            if has_row:
                return True
            else:
                pass
        return False

    def has_vertical_line(self):
        """
        Determine if a BingoCard has a vertical line stamped out
        :return: true if a vertical line is stamped out, false otherwise
        """
        # check column
        for j in range(5):
            has_column = True
            # check column entries
            for i in range(5):
                if self.__card[i][j] != 0:
                    has_column = False
                    break
                else:
                    pass
            if has_column:
                return True
            else:
                pass
        return False

    def has_diagonal_line(self):
        """
        Determine if a BingoCard has a diagonal line stamped out
        :return: true if a diagonal line is stamped out, false otherwise
        """
        # check top-left to bottom-right diagonal
        has_diagonal = True
        for i in range(5):
            if self.__card[i][i] != 0:
                has_diagonal = False
                break
        if has_diagonal:
            return True
        # check bottom-left to top-right diagonal
        else:
            for j in range(5):
                if self.__card[j][4-j] != 0:
                    return False
                else:
                    pass
            return True

    def has_line(self):
        """
        Determine if a BingoCard has a line of any kind stamped out
        :return: true if a line is stamped out, false otherwise
        """
        return self.has_horizontal_line() or self.has_vertical_line() or self.has_diagonal_line()

    def has_blackout(self):
        """
        Determine if a BingoCard is completely stamped out
        :return: true if everything is stamped out, false otherwise
        """
        for i in range(5):
            for j in range(5):
                if self.__card[i][j] != 0:
                    return False
                else:
                    pass
        return True

    def __repr__(self):
        """
        Make a representation of the BingoCard that looks exactly like
        the way one would make it in code
        :return: a string representation of the code necessary to make the BingoCard
        """
        return f"{self.__class__.__name__}(\"{self.__name}\")"

    def __str__(self):
        """
        Return a string representation of the BingoCard
        :return: a string representation of the BingoCard
        """
        st = "+--+--+--+--+--+\n"
        # make each row of the bingo card
        for i in range(5):
            for j in range(5):
                st += "|"
                if len(str(self.__card[i][j])) == 1:
                    if self.__card[i][j] == 0:
                        st += "  "
                    else:
                        st += "0" + str(self.__card[i][j])
                else:
                    st += str(self.__card[i][j])
            st += "|\n"
            st += "+--+--+--+--+--+\n"
        # set up name
        if len(self.__name) > 16:
            display_name = self.__name[0: 16]
        else:
            display_name = self.__name + (16 - len(self.__name)) * " "
        st += display_name + "\n"
        return st

    @staticmethod
    def print_cards(list_of_cards):
        """
        Print BingoCards in a row for making all BingoCards easy to see at once
        :param list_of_cards: a list of BingoCards
        :postcond: the BingoCards are printed to the console all in a row
        """
        for c in range(len(list_of_cards)):
            print("+--+--+--+--+--+  ", end="")
        print()
        # print each row of each bingo card
        for i in range(5):
            for cr in list_of_cards:
                for j in range(5):
                    print("|", end="")
                    if len(str(cr.card[i][j])) == 1:
                        if cr.card[i][j] == 0:
                            print("  ", end="")
                        else:
                            print("0" + str(cr.card[i][j]), end="")
                    else:
                        print(str(cr.card[i][j]), end="")
                print("|  ", end="")
            print()
            for d in range(len(list_of_cards)):
                print("+--+--+--+--+--+  ", end="")
            print()
        # print names
        for crd in list_of_cards:
            if len(crd.name) > 16:
                print(crd.name[0: 16], end="  ")
            else:
                print(crd.name + (16 - len(crd.name)) * " ", end="  ")
        print()
        print()


if __name__ == "__main__":
    print("Test suite for bingo_card.py")

    bc = BingoCard("Jackson")

    print(bc.__repr__())
    print(bc)

    bc.stamp_number(1)
    bc.stamp_number(2)
    bc.stamp_number(3)
    bc.stamp_number(4)
    bc.stamp_number(5)

    bc.stamp_number(16)
    bc.stamp_number(17)
    bc.stamp_number(18)
    bc.stamp_number(19)
    bc.stamp_number(20)

    bc.stamp_number(31)
    bc.stamp_number(32)
    bc.stamp_number(33)
    bc.stamp_number(34)
    bc.stamp_number(35)

    bc.stamp_number(46)
    bc.stamp_number(47)
    bc.stamp_number(48)
    bc.stamp_number(49)
    bc.stamp_number(50)

    bc.stamp_number(61)
    bc.stamp_number(62)
    bc.stamp_number(63)
    bc.stamp_number(64)
    bc.stamp_number(65)

    print(bc)

    card1 = BingoCard("Player 1")
    card2 = BingoCard("A")
    card3 = BingoCard("0123456789ABCDEF")
    card4 = BingoCard("This name is too long")
    card5 = BingoCard("")

    cards = [card1, card2, card3, card4, card5]
    BingoCard.print_cards(cards)

    # sample game
    order_of_numbers = rand.sample(range(1, 76), 75)
    has_any_line = False
    has_h_line = False
    has_v_line = False
    has_d_line = False
    has_b = False

    for number in order_of_numbers:
        for card in cards:
            card.stamp_number(number)
            if not has_any_line:
                if card.has_line():
                    has_any_line = True
                    print(card.name + " has the first line!")
                    BingoCard.print_cards(cards)
                else:
                    pass
            if not has_h_line:
                if card.has_horizontal_line():
                    has_h_line = True
                    print(card.name + " has the first horizontal line!")
                    BingoCard.print_cards(cards)
                else:
                    pass
            if not has_v_line:
                if card.has_vertical_line():
                    has_v_line = True
                    print(card.name + " has the first vertical line!")
                    BingoCard.print_cards(cards)
                else:
                    pass
            if not has_d_line:
                if card.has_diagonal_line():
                    has_d_line = True
                    print(card.name + " has the first diagonal line!")
                    BingoCard.print_cards(cards)
                else:
                    pass
            if not has_b:
                if card.has_blackout():
                    has_b = True
                    print(card.name + " has the first blackout!")
                    BingoCard.print_cards(cards)
                else:
                    pass
    print("All numbers called.")
    BingoCard.print_cards(cards)

    print("Testing complete!")
