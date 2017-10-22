import datetime as dt
import time
import numpy as np
from sklearn.ensemble import RandomForestRegressor

from backend import app, db
from models import User, Song, UserSong
from flask import request, jsonify

import spotipy_helper as sph
import model_helper as mdh


@app.route('/v1.0/song', methods=['POST'])
def song_meta():

    song = request.json
    spot_id = sph.get_song(song)

    user = User.query.get(1)

    song_db = Song.query.filter_by(spot_id=spot_id).first()
    if not song_db:
        song_features = sph.get_features(spot_id)

        print song_features

        song_db = mdh.set_features(song_features)

        db.session.add(song_db)
        db.session.commit()

    UserSong(user, song_db, dt.now())
    db.session.commit()

    response = {"success": True}

    return jsonify(response)

@app.route('/v1.0/get_recommendation', methods=['GET'])
def recommend():

    start = time.time()
    user = User.query.get(1)

    time7 = dt.datetime.now() - dt.timedelta(days=7)
    timen = dt.datetime.now()

    songs = map(lambda x: x.song, UserSong.query.filter_by(user=user).
                filter((UserSong.time_played >= time7) & (UserSong.time_played <= timen)).join(Song))

    songs_modified, labels = np.unique(songs, return_counts=True)

    songs_features = mdh.get_features(songs_modified)
    songs_labels = labels.astype('float')/labels.sum()
    #
    clf = RandomForestRegressor()
    clf.fit(songs_features, songs_labels)

    song_count = Song.query.count()

    preds_all = np.zeros((song_count, 2))

    for i in range(1, song_count, 50000):
        songs_db = Song.query.filter(Song.id >= i, Song.id < i + 50000).all()

        song_db_features = mdh.get_features(songs_db)

        preds = clf.predict(song_db_features)

        preds_all[i - 1: min(i + 49999, song_count), 1] = preds

        preds_all[i - 1: min(i + 49999, song_count), 0] = np.array(range(i, min(i + 50000, song_count + 1)))

        sendind = preds_all[1].argsort()[-10:]

        sendable_ids = preds_all[sendind, 0].tolist()

        spot_ids = [Song.query.with_entities(Song.spot_id).filter_by(id=id).first() for id in sendable_ids]

        tracks = sph.get_songs(spot_ids)

    return



