import datetime

from backend import app, db
from models import User, Song
from flask import request, jsonify

import spotipy_helper as sph
import model_helper as mdh


@app.route('/v1.0/song', methods=['POST'])
def song_meta():

    song = request.json
    spot_id = sph.get_song(song)

    user = User.query.get(0)

    song_db = Song.query.filter_by(spot_id=spot_id).first()
    if not song_db:
        song_features = sph.get_features(spot_id)

        song_db = mdh.set_features(song_features)

        db.session.add(song_db)
        db.session.commit()

    user.plays.append(song_db, )

    response = {"success": True}

    return jsonify(response)

    

