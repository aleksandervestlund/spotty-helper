from collections.abc import Mapping, Sequence
from typing import Any

from spotipy import Spotify

from source.comparators import COMPARATORS
from source.remove_duplicates import remove_duplicates
from source.remove_unavailable import remove_unavailable
from source.sort_playlist import sort_playlist


def process_playlists(
    sp: Spotify, playlists: Sequence[Mapping[str, Any]]
) -> None:
    for playlist in playlists:
        name = playlist["name"]
        id_ = playlist["id"]
        print(f"Processing playlist {name!r}...")
        remove_duplicates(id_, sp)
        # remove_unavailable(id_, sp)

        if (sorting := COMPARATORS.get(name)) is None:
            print(f"Not sorting {name!r} as it has no comparator.")
        else:
            sort_playlist(id_, sorting, sp)
