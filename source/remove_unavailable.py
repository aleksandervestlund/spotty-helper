from spotipy import Spotify

from source.fetch_all_items import get_all_playlist_tracks


def remove_unavailable(playlist_id: str, sp: Spotify) -> None:
    tracks = get_all_playlist_tracks(playlist_id, sp)

    for track in tracks:
        if not track["track"]["is_local"]:
            continue

        uri = track["track"]["uri"]
        print(f"Removing unavailable song {track['track']['name']!r}...")
        # sp.playlist_remove_all_occurrences_of_items(playlist_id, [uri])
