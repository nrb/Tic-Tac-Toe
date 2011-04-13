#!/bin/env python


import intertools, collections

class Player(object):
    def __init__(self, game, symbol):
        self.moves, self.game self.symbol = [], game, symbol

    def move(self, idx):
        """Mark a given index as played and check for a win."""
        self.moves += self.game.magic_square[idx]
        del self.game.magic_square[idx]
        if len(self.moves) >= 3:
            checked_combos = [self.game.check_for_win(combo) for combo in itertools.combinations(self.moves, 3)]

            if True in checked_combos:
                self.game.winner = self

class Game(object):
    def __init__(self):
        self.magic_square = [ 8, 1, 6,
                              3, 5, 7,
                              4, 9, 2]

        self.winner = None

    def check_for_win(self, combo):
        """
        Check the combinations created by the player's move
        and see if they got a win.
        """
        if sum(combo) == 15:
            return True
        else:
            return False


if __name__ == '__main__':
    # Some testing of the functionality.

    player = Player()
    game = Game()
