import os

from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from source.playlists import PLAYLISTS
from source.remove_duplicates import remove_duplicates
from source.sort_playlist import sort_playlist


load_dotenv()


def main() -> None:
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
    sp = Spotify(auth_manager=auth)
    playlists = sp.user_playlists("aleksander2001")["items"]  # type: ignore

    for playlist in playlists:
        name = playlist["name"]
        id_ = playlist["id"]

        if (sorting := PLAYLISTS.get(name)) is None:
            print(f"Skipping playlist {name!r} as it has no sorting function.")
            continue

        print(f"Processing playlist {name!r}...")
        remove_duplicates(id_, sp)
        sort_playlist(id_, sorting, sp)


if __name__ == "__main__":
    main()
