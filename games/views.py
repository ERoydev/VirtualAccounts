from django.shortcuts import render

from django.http import JsonResponse
from games.services.twitch_api import get_twitch_user_info, get_popular_multiplayer_games


# Create your views here.

def get_twitch_user_view(request, username):
    try:
        user_info = get_twitch_user_info(username)
        return JsonResponse(user_info, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


