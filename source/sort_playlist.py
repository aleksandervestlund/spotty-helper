from collections.abc import Callable
from typing import Any

from spotipy import Spotify

from source.fetch_all_items import get_all_playlist_tracks


def sort_playlist(
    playlist_id: str,
    comparator: Callable[[tuple[str, str, str]], Any],
    sp: Spotify,
) -> None:
    tracks = get_all_playlist_tracks(playlist_id, sp)
    track_ids = [item["track"]["id"] for item in tracks]
    sorted_tracks: list[tuple[str, str, str]] = sorted(
        (
            (
                item["track"]["id"],
                item["track"]["name"],
                item["track"]["artists"][0]["name"],
            )
            for item in tracks
        ),
        key=comparator,
    )

    if None in track_ids:
        print("Skipping sorting playlist as it contains local tracks.")
        return

    for j, (track_id, track_name, track_artist) in enumerate(sorted_tracks):
        if (i := track_ids.index(track_id)) == j:
            continue

        # Positions in Spotify are 1-indexed
        print(
            f"Moving song {track_name!r} by {track_artist!r} from position "
            f"{i + 1} to position {j + 1}..."
        )
        track_ids.pop(i)
        track_ids.insert(j, track_id)
        sp.playlist_reorder_items(playlist_id, i, j)

    print("Playlist sorted without modifying 'Date added'.")
    print()
