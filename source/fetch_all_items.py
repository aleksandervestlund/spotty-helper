from collections.abc import Callable, Mapping, Sequence
from typing import Any

from spotipy import Spotify


def _fetch_all_items(
    fetch_func: Callable[[str], Mapping[str, Any]], sp: Spotify, *args: Any
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    results = fetch_func(*args)
    items.extend(results["items"])

    while results["next"] is not None:
        results: Mapping[str, Any] = sp.next(results)  # type: ignore
        items.extend(results["items"])

    return items


def get_all_playlist_tracks(
    playlist_id: str, sp: Spotify
) -> list[dict[str, Any]]:
    return _fetch_all_items(sp.playlist_tracks, sp, playlist_id)  # type: ignore


def get_all_playlists(user: str, sp: Spotify) -> Sequence[Mapping[str, Any]]:
    return _fetch_all_items(sp.user_playlists, sp, user)  # type: ignore
