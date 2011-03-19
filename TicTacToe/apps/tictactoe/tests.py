"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

from TicTacToe.apps.tictactoe.models import Game


class GameTest(TestCase):
    def setUp(self):
        self.g = Game(test=True)

    def test_matrix_list(self):
        '''
        Make sure that the matrix is initialized correctly.
        '''
        self.assertEqual([['-', '-', '-']] * 3, self.g.matrix)

    def test_marking(self):
        '''
        '''
        self.g.mark(0,0, 'x')
        self.g.mark(2,2, 'o')

        self.assertEqual('x', self.g.matrix[0][0])
        self.assertEqual('o', self.g.matrix[2][2])

    def test_failing_marks(self):
        self.assertRaises(ValueError, self.g.mark, 0, 0, 'a')
        self.assertRaises(ValueError, self.g.mark, 2, 2, 'b')

    def test_turn_toggle(self):
        self.g.mark(0,0,'x')

        self.assertEqual(self.g.players_turn, 'o')

    def test_no_double_turn(self):
        # Disable testing mode, since it blocks the exception.
        self.g.test = False
        self.g.mark(0,0,'x')
        self.assertRaises(Game.IllegalMove, self.g.mark, 0, 1, 'x')

    def test_no_overwrite_marks(self):
        '''No cell should be overwritten if it already contains
        a player mark.'''

        self.g.mark(0, 0, 'x')
        self.g.mark(0, 0, 'o')
        self.assertEqual(self.g.matrix[0][0], 'x')

