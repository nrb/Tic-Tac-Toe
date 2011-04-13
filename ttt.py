#!/bin/env python


import itertools, collections

class Player(object):
    def __init__(self, game, symbol):
        self.moves, self.game, self.symbol = [], game, symbol

    def move(self, idx):
        """Mark a given index as played and check for a win."""
        self.moves.append(self.game.magic_square[idx])

        # Mark the space as None, cause deleting it shifts the indices.
        self.game.magic_square[idx] = None
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

    game = Game()
    player1 = Player(game, 'X')
    player2 = Player(game, 'O')

    player1.move(0)
    assert 8 not in game.magic_square
    assert 8 in player1.moves

    player2.move(4)
    assert 5 not in game.magic_square
    assert 5 in player2.moves
