import datetime

from backend import app
from flask import Flask, render_template, request, jsonify

import spotipy_helper as sph


@app.route('/v1.0/song', methods=['POST'])
def song_meta():
    # data = request.form.to_dict()
    song = request.json

    spot_id = sph.get_song(song)

    features = sph.get_features(spot_id)

    return jsonify(features)

    

