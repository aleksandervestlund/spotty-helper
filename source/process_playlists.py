from collections.abc import Mapping, Sequence
from typing import Any

from spotipy import Spotify

from source.comparators import COMPARATORS
from source.remove_duplicates import remove_duplicates
from source.remove_unavailable import remove_unavailable
from source.sort_playlist import sort_playlist


def process_playlists(
    playlists: Sequence[Mapping[str, Any]], sp: Spotify
) -> None:
    for playlist in playlists:
        name = playlist["name"]
        playlist_id = playlist["id"]

        print()
        print(f"Processing playlist {name!r}...")

        remove_unavailable(playlist_id, sp)
        remove_duplicates(playlist_id, sp)

        if (comparator := COMPARATORS.get(name)) is None:
            print(f"Not sorting {name!r} as it has no comparator.")
        else:
            sort_playlist(playlist_id, comparator, sp)
