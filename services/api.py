import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()

# TOKEN = os.getenv('TOKEN')

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
username = os.getenv('USERNAME')

# note that I extended the scope to also modify non-public playlists
scope = "playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-read-private user-top-read streaming user-library-read user-read-currently-playing user-follow-read user-modify-playback-state user-read-recently-played"

redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                      client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

token = spotipy.util.prompt_for_user_token(
    username, scope, client_id, client_secret, redirect_uri)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

# Only for test pourpose
results = sp.current_user_recently_played(limit=50, after=None, before=None)
print((json.dumps(results, indent=4)))
