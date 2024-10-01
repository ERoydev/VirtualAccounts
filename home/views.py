from django.shortcuts import render

from games.services.twitch_api import get_popular_multiplayer_games


# Create your views here.

def index(request):
    try:
        popular_games = get_popular_multiplayer_games(8)

        # Only create context if successful
        context = {
            'games': popular_games
        }
        return render(request, 'home/home.html', context)
    except Exception as e:
        # In case of an error, render the template without context
        return render(request, 'home/home.html')