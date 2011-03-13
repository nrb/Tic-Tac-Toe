from django.db import models

class Game(object):
    '''
    Captures the state of the game board, so that it may be maintained
    between requests.
    '''

    def __init__(self):
        # Create a 3 x 3 matrix that we use as the markers.
        self.matrix = [['-', '-', '-']] * 3

    def mark(self, row, column, character):
        '''
        Tag the cell that the player marked with their character.

        Only 'x' and 'o' are allowed.  Also, only currently-blank
        cells can be marked.
        '''
        if character not in ['x', 'o']:
            raise ValueError, "Character's value should be either x or o."

        # Make sure we're marking only blank cells.
        if self.matrix[row][column] == '-':
            self.matrix[row][column] = character
        else:
            return

    def check_win_conditions(self):
        '''
        Checks to see which player won.

        We have to check for horizontal, vertical, and diagonal cases.

        Also, it should check for stalemates (that is, the board is full
        without anyone getting 3 touching). In that case, the player
        with the most marks wins.
        '''
        # Horizontal
        for row in self.matrix:
            if ['x'] * 3 == row:
                return 'x'
            elif ['o'] * 3 == row:
                return 'o'

        # Pivot matrix to check columns in a more readable way
        # To do so, initiate another blank game board.
        pivoted_matrix = [['-', '-', '-']] * 3
        for column in xrange(0, 3):
            for row in matrix:
                # Invert the column and rows to do the pivot
                pivoted_matrix[column][row] = matrix[row][column]

        # Check the newly pivoted board.
        for row in pivoted_matrix:
            if ['x'] * 3 == row:
                return 'x'
            elif ['o'] * 3 == row:
                return 'o'

        # TODO: Diagonals, should be 2.
        # TODO: Stalemates

        # If no win conditions met, we return nothing and keep going.
        return None
    
    def retart(self):
        pass

