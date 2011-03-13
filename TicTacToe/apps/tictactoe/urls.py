from django.conf.urls.defaults import *

urlpatterns = patterns('TicTacToe.apps.tictactoe.views',
        url(r'^$', 'game_board', name='game_board')
)
