from django.template import RequestContext
from django.shortcuts import render_to_response

def game_board(request):
    context = RequestContext(request,{})
    return render_to_response('tictactoe/game_board.html', context)

