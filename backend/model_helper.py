"""
Helpers for inserting data in the database, especially with songs.
"""

import numpy as np

from models import Song


def set_features(song_features):
    """
    Accepts song_features. Creates Song object and returns it
    """

    song = Song(
        spot_id=song_features.get('id'),
        dance=song_features.get('danceability', 0) or 0,
        energy=song_features.get('energy', 0) or 0,
        key=song_features.get('key', 0) or 0,
        loud=song_features.get('loudness', 0) or 0,
        mode=song_features.get('mode', 0) or 0,
        speech=song_features.get('speechiness', 0) or 0,
        acoustic=song_features.get('acousticness', 0) or 0,
        instrument=song_features.get('instrumentalness', 0) or 0,
        live=song_features.get('liveness', 0) or 0,
        valence=song_features.get('valence', 0) or 0,
        tempo=song_features.get('tempo', 0) or 0,
        duration=song_features.get('duration_ms', 0) or 0,
        time=song_features.get('time_signature', 0) or 0
    )

    return song

def get_features(songs):

    array_shape = (len(songs), 13)

    song_features = np.zeros(array_shape)

    for i,song in enumerate(songs):
        song_features[i, 0] = song.dance
        song_features[i, 1] = song.energy
        song_features[i, 2] = song.key
        song_features[i, 3] = song.loud
        song_features[i, 4] = song.mode
        song_features[i, 5] = song.speech
        song_features[i, 6] = song.acoustic
        song_features[i, 7] = song.instrument
        song_features[i, 8] = song.live
        song_features[i, 9] = song.valence
        song_features[i, 10] = song.tempo
        song_features[i, 11] = song.duration
        song_features[i, 12] = song.time

    return song_features