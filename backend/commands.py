"""
Module for custom commands especially loading the song features
"""

import os
import json

import click
from backend import app, db
from backend.models import Song

import model_helper as mdh

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

                        s = mdh.set_features(song)

                        db.session.add(s)
            db.session.commit()

    print "Done"
    return



