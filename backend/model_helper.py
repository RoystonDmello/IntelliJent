"""
Helpers for inserting data in the database, especially with songs.
"""

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