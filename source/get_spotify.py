import os

from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


load_dotenv(verbose=True)


def get_spotify() -> Spotify:
    scopes = (
        "playlist-modify-private",
        "playlist-modify-public",
        "playlist-read-collaborative",
        "playlist-read-private",
    )
    auth = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=" ".join(scopes),
    )
    return Spotify(auth_manager=auth)
