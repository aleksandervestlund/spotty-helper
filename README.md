# Spotty-helper

> Created by: Aleksander Thornes Vestlund

This is a helper tool for Spotify, created to help manage playlists.
The tool is able to remove all duplicates,
find all songs that have been removed from Spotify, as well as sort playlists based on their comparators.

> [Sort Your Music](http://sortyourmusic.playlistmachinery.com/index.html) is also a great tool for sorting playlists based on different parameters,
but it does not support maintaining the `Date added`-field for playlists greater than 100 songs.

## Table of contents

- [Getting started](#getting-started)

## Getting started

- Make sure you have Python ≥ 3.10 installed.

- Clone the repository.

- Install the required packages by running the following command either locally or in a virtual environment:

```bash
pip install -r requirements.txt`
```

- Create a `comparators.py` file in the `source`-directory.
This file should contain a mapping of playlist-names to their respective comparators.
This can be done by executing the following command:

```bash
echo "COMPARATORS = {}" > source/comparators.py
```

> Use `/` on Unix-like systems and `\` on Windows.

- Run the `main`-function by using the running the following command, while remembering to change out the `user`-argument passed to `get_all_playlists` in the `main`-function with your own Spotify username:

```bash
python main.py
```

> It might be the case that you need to run the commands with `pip3` and `python3` instead of `pip` and `python`.
