from spotipy import Spotify

from source.get_all_playlist_tracks import get_all_playlist_tracks


def remove_duplicates(playlist_id: str, sp: Spotify) -> None:
    tracks = get_all_playlist_tracks(playlist_id, sp)
    track_ids = [item["track"]["id"] for item in tracks]
    track_names = [item["track"]["name"] for item in tracks]
    track_artist = [item["track"]["artists"][0]["name"] for item in tracks]

    duplicate_ids = {
        track_id for track_id in track_ids if track_ids.count(track_id) > 1
    }

    if not duplicate_ids:
        print("No duplicate songs found.")
        return

    print("Duplicate songs found and will be removed.")
    for track_id in duplicate_ids:
        # The API kept removing all occurrences of the track, even though the
        # function was using `playlist_remove_specific_occurrences_of_items`
        # and the `positions` parameter. Therefore, it now removes all
        # occurrences and then adds one back

        idx = track_ids.index(track_id)
        uri = tracks[idx]["track"]["uri"]

        print(f"Name={track_names[idx]}; Artist={track_artist[idx]}")
        sp.playlist_remove_all_occurrences_of_items(playlist_id, [uri])
        sp.playlist_add_items(playlist_id, [uri], position=[idx])
