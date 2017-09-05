from backend import app
from flask import Flask, render_template, request, jsonify


@app.route('/v1.0/song', methods=['POST'])
def song_meta():
    # data = request.form.to_dict()
    song = request.json

    spot_id = sp.get_song(song)

    features = sp.get_features(spot_id)

    return jsonify(features)

    

