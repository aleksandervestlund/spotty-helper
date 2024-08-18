from source.comparators import COMPARATORS
from source.fetch_all_items import get_all_playlists
from source.get_spotify import get_spotify
from source.process_playlists import process_playlists


def main() -> None:
    sp = get_spotify()
    playlists = get_all_playlists("aleksander2001", sp)

    if comp := set(COMPARATORS) - {playlist["name"] for playlist in playlists}:
        print(f"These playlists are unknown: {', '.join(comp)}.")
    else:
        process_playlists(playlists, sp)


if __name__ == "__main__":
    main()
