import os


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import spotipy as sp
import spotipy.util as util


from config import credentials


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

username, scope, client_id, client_secret, redirect_uri = credentials

cache_filename = ".cache-{0}".format(username)
if os.path.isfile(cache_filename):
    os.remove(cache_filename)

token = util.prompt_for_user_token(username, scope,
                                       client_id, client_secret,
                                       redirect_uri)

spotify = sp.Spotify(auth=token)

from backend import views, models