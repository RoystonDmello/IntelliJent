from backend import app
from flask import Flask, render_template, request, jsonify


@app.route('/v1.0/song', methods=['POST'])
def song_meta():
    # data = request.form.to_dict()
    song = request.json

