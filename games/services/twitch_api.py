import requests
import os

# Ideally, load sensitive values from environment variables
CLIENT_ID = 'h99ayv98oyhqed1bknma67wpmnftki'
CLIENT_SECRET = 'w9pe6iiw08cpx9yl005rd3fiumcz0l'

def get_twitch_access_token():
    # Method used to get access_token to perform request to the api
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Failed to get access token: {response.status_code} - {response.text}")

def get_twitch_user_info(username):
    access_token = get_twitch_access_token()
    url = f"https://api.twitch.tv/helix/users"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Client-Id': CLIENT_ID
    }
    params = {
        'login': username
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get user info: {response.status_code} - {response.text}")


def get_popular_multiplayer_games(data_limit):
    url = "https://api.igdb.com/v4/games"
    access_token = get_twitch_access_token()
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}',
    }
    # The query to get popular games
    data = f"""
     fields name, rating, rating_count, hypes, multiplayer_modes.*, genres.name, first_release_date, cover.url, summary;
    where multiplayer_modes.onlinecoop = true 
      & (genres.name = "Role-playing (RPG)" | genres.name = "Adventure" | genres.name = "MMORPG" | genres.name = "Shooter") 
      & (rating > 80 | hypes > 100)
      & rating_count > 50;
    sort rating desc;
    limit {data_limit};
    """
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch games: {response.status_code} - {response.text}")
