#!/bin/env python


import intertools, collections

class Player(object):
    def __init__(self, symbol):
        self.moves, self.symbol = [], symbol

    def move(self, idx):
        """Mark a given index as played and check for a win."""
        pass

class Game(object):
    magic_square = [ 8, 1, 6,
                     3, 5, 7,
                     4, 9, 2]

    def check_for_win(self, combo):
        """
        Check the combinations created by the player's move
        and see if they got a win.
        """
        pass


if __name__ == '__main__':
    # Some testing of the functionality.

    player = Player()
    game = Game()
