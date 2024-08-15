import os

from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from source.remove_duplicates import remove_duplicates
from source.sort_playlist import sort_playlist


load_dotenv()


def main() -> None:
    scopes = (
        "playlist-modify-private",
        "playlist-modify-public",
        "playlist-read-private",
    )
    auth = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=" ".join(scopes),
    )
    sp = Spotify(auth_manager=auth)

    api_playground_id = "4PtF2eIciT6a3y2sLZfDxH"

    remove_duplicates(api_playground_id, sp)
    sort_playlist(
        api_playground_id, lambda x: (x[2].lower(), x[3].lower(), x[1]), sp
    )


if __name__ == "__main__":
    main()
