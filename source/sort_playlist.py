from collections.abc import Callable
from typing import Any

from spotipy import Spotify

from source.get_all_playlist_tracks import get_all_playlist_tracks


def sort_playlist(
    playlist_id: str,
    sorting: Callable[[tuple[str, str, str]], Any],
    sp: Spotify,
) -> None:
    tracks = get_all_playlist_tracks(playlist_id, sp)
    track_ids = [item["track"]["id"] for item in tracks]
    sorted_tracks: list[tuple[str, str, str]] = [
        (
            item["track"]["id"],
            item["track"]["name"],
            item["track"]["artists"][0]["name"],
        )
        for item in tracks
    ]
    sorted_tracks.sort(key=sorting)

    if None in track_ids:
        print("Skipping playlist as it contains local tracks.")
        return

    modified = False
    for j, (track_id, track_name, track_artist) in enumerate(sorted_tracks):
        if (i := track_ids.index(track_id)) == j:
            if modified:
                # If the playlist is already sorted, this will never be printed
                print(
                    f"Song {track_name!r} by {track_artist!r} correctly "
                    f"placed at {i + 1}."
                )
            continue

        if not modified:
            print("Reordering playlist...")
            modified = True

        print(
            f"Moving song {track_name!r} by {track_artist!r} from position "
            f"{i + 1} to position {j + 1}..."
        )
        track_ids.pop(i)
        track_ids.insert(j, track_id)
        sp.playlist_reorder_items(playlist_id, i, j)

    if modified:
        print("Playlist sorted without modifying 'Date added'.")
    else:
        print("Playlist already sorted.")
