from spotipy import Spotify

from source.fetch_all_items import get_all_playlist_tracks


def remove_unavailable(playlist_id: str, sp: Spotify) -> None:
    tracks = get_all_playlist_tracks(playlist_id, sp)

    for track in tracks:
        track_info = track["track"]
        if track_info["is_local"]:
            continue
        if track_info["available_markets"]:
            continue
        if track_info["preview_url"] is not None:
            continue

        uri = track_info["uri"]
        print(
            f"Removing unavailable song {track_info['name']!r} by "
            f"{track_info['artists'][0]['name']!r}..."
        )
        sp.playlist_remove_all_occurrences_of_items(playlist_id, [uri])
