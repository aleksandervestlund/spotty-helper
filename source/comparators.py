def artist_name_id(x: tuple[str, str, str]) -> tuple[str, str, str]:
    return (x[2].lower(), x[1].lower(), x[0])


def name_artist_id(x: tuple[str, str, str]) -> tuple[str, str, str]:
    return (x[1].lower(), x[2].lower(), x[0])


COMPARATORS = {
    "big pp": name_artist_id,
    "ferrari": name_artist_id,
    "Hvite menn som pusher 50": artist_name_id,
    "juice leaked/unreleased": name_artist_id,
    "juice": name_artist_id,
    "Know 'Em All!": artist_name_id,
    "LaroiTheKidd": name_artist_id,
    "nathan fillion": name_artist_id,
}
