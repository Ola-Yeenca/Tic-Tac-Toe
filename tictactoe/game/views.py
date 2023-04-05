from django.shortcuts import render, redirect
from .models import Game
from .forms import MoveForm

def board(request):
    game = Game(state='         ', turn='X')
    game.save()
    form = MoveForm()
    context = {
        'game': game,
        'form': form,
    }
    return render(request, 'game/board.html', context)

def move(request, game_id):
    game = Game.objects.get(id=game_id)
    form = MoveForm(request.POST)
    if form.is_valid():
        position = form.cleaned_data['position']
        if game.state[position] == ' ':
            state = list(game.state)
            state[position] = game.turn
            game.state = ''.join(state)
            if game.turn == 'X':
                game.turn = 'O'
            else:
                game.turn = 'X'
            game.save()
    return redirect('board')
