from collections.abc import Callable
from typing import Any

from spotipy import Spotify

from source.get_all_playlist_tracks import get_all_playlist_tracks


def sort_playlist(
    playlist_id: str,
    sorting: Callable[[tuple[int, str, str, str]], Any],
    sp: Spotify,
) -> None:
    tracks = get_all_playlist_tracks(playlist_id, sp)
    track_details: list[tuple[int, str, str, str]] = [
        (
            i,
            item["track"]["id"],
            item["track"]["name"],
            item["track"]["artists"][0]["name"],
        )
        for i, item in enumerate(tracks)
    ]

    # Sort tracks by name, then artist, then id
    sorted_tracks = sorted(track_details, key=sorting)
    new_positions = {i: sorted_tracks[i][0] for i in range(len(sorted_tracks))}

    print("Reordering playlist...")
    for new_index, (original_index, _, track_name, track_artist) in enumerate(
        sorted_tracks
    ):
        if original_index != new_index:
            print(
                f"Moving track (name={track_name}, artist={track_artist}) "
                f"from index {original_index} to index {new_index}."
            )
            sp.playlist_reorder_items(playlist_id, original_index, new_index)

            # After moving a track, all subsequent indices shift by one
            # Therefore, update the new_positions map
            new_positions = {
                k: (v - 1 if v > original_index else v)
                for k, v in new_positions.items()
            }

    print("Playlist sorted without changing 'Date added'.")
