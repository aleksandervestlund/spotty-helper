from spotipy import Spotify

from source.fetch_all_items import get_all_playlist_tracks


def chunk_list(lst: list, n: int = 100) -> list[list[str]]:
    return [lst[i : i + n] for i in range(0, len(lst), n)]
    # return itertools.batched(lst, n)  # Python 3.12+


def remove_unavailable(playlist_id: str, sp: Spotify) -> None:
    tracks = get_all_playlist_tracks(playlist_id, sp)
    uris: list[str] = []

    for track in tracks:
        track_info = track["track"]

        if track_info["available_markets"]:
            continue
        if track_info["preview_url"] is not None:
            continue
        if track_info["is_local"]:
            continue

        print(
            f"Removing unavailable song {track_info['name']!r} by "
            f"{track_info['artists'][0]['name']!r}..."
        )
        uris.append(track_info["uri"])

    if not uris:
        print("No unavailable songs found.")
        return

    for chunk in chunk_list(uris):
        sp.playlist_remove_all_occurrences_of_items(playlist_id, chunk)
