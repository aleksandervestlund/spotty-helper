from typing import Any

from spotipy import Spotify


def get_all_playlist_tracks(
    playlist_id: str, sp: Spotify
) -> list[dict[str, Any]]:
    tracks: list[dict[str, Any]] = []
    results: dict[str, Any] = sp.playlist_tracks(playlist_id)  # type: ignore
    tracks.extend(results["items"])

    while results["next"]:
        results = sp.next(results)  # type: ignore
        tracks.extend(results["items"])

    return tracks
