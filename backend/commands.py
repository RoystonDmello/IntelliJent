"""
Module for custom commands especially loading the song features
"""

import os
import json

import click
from backend import app, db
from backend.models import Song

@app.cli.command()
def load_songs():
    """
    Loads the song features in the database.
    :return: None
    """
    spot_ids = set()
    print "The modified one is being run"

    data_dir = '/home/royston/IntelliJent/results'

    for filename in sorted(os.listdir(data_dir)):
        filepath = os.path.join(data_dir, filename)

        with open(filepath) as fp:
            data = json.load(fp)

            click.echo(filepath)

            for song in data:
                if song:

                    if not song.get('id') in spot_ids:

                        spot_ids.add(song.get('id'))

                        s = Song(
                            spot_id=song.get('id'),
                            dance=song.get('danceability', 0) or 0,
                            energy=song.get('energy', 0) or 0,
                            key=song.get('key', 0) or 0,
                            loud=song.get('loudness', 0) or 0,
                            mode=song.get('mode', 0) or 0,
                            speech=song.get('speechiness', 0) or 0,
                            acoustic=song.get('acousticness', 0) or 0,
                            instrument=song.get('instrumentalness', 0) or 0,
                            live=song.get('liveness', 0) or 0,
                            valence=song.get('valence', 0) or 0,
                            tempo=song.get('tempo', 0) or 0,
                            duration=song.get('duration_ms', 0) or 0,
                            time=song.get('time_signature', 0) or 0
                        )

                        db.session.add(s)
            db.session.commit()

    print "Done"
    return



