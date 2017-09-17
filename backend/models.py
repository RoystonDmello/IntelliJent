from sqlalchemy.ext.associationproxy import association_proxy

from backend import db


# plays = db.Table('plays',
#             db.Column('user_id', db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
#             db.Column('song_id', db.Integer(), db.ForeignKey('song.id', ondelete='RESTRICT'), primary_key=True),
#             db.Column('time_played', db.DateTime(), primary_key=True)
#         )

class UserSong(db.Model):
    __tablename__ = 'user_song'
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    song_id = db.Column('song_id', db.Integer(), db.ForeignKey('song.id', ondelete='RESTRICT'), primary_key=True)

    time_played = db.Column('time_played', db.DateTime(), primary_key=True)

    user = db.relationship("User", backref=db.backref('user_song'))

    song = db.relationship("Song")

    def __init__(self, user, song, time_played):
        self.user = user
        self.song = song
        self.time_played = time_played

    def __repr__(self):
        return '<User %s Song %s>' % (self.user.username, self.song.spot_id)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pswd_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100))
    songs = association_proxy('user_song','song')
    # TO be switche when number of users far exceeds average number of plays

    def __init__(self, username, email, pswd_hash):
        self.username = username
        self.email = email
        self.pswd_hash = pswd_hash

    def __repr__(self):
        return '<User %s>' % self.username


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spot_id = db.Column(db.String(50), unique=True, nullable=False)
    dance = db.Column(db.Float(), nullable=False)
    energy = db.Column(db.Float(), nullable=False)
    key = db.Column(db.Integer(), nullable=False)
    loud = db.Column(db.Float(), nullable=False)
    mode = db.Column(db.Integer(), nullable=False)
    speech = db.Column(db.Float(), nullable=False)
    acoustic = db.Column(db.Float(), nullable=False)
    instrument = db.Column(db.Float(), nullable=False)
    live = db.Column(db.Float(), nullable=False)
    valence = db.Column(db.Float(), nullable=False)
    tempo = db.Column(db.Float(), nullable=False)
    duration = db.Column(db.Integer(), nullable=False)
    time = db.Column(db.Integer(), nullable=False)

    def __init__(self, spot_id, dance, energy, key, loud, mode, speech, acoustic,
                 instrument, live, valence, tempo, duration, time):
        self.spot_id = spot_id
        self.dance = dance
        self.energy = energy
        self.key = key
        self.loud = loud
        self.mode = mode
        self.speech = speech
        self.acoustic = acoustic
        self.instrument = instrument
        self.live = live
        self.valence = valence
        self.tempo = tempo
        self.duration = duration
        self.time = time

    def __repr__(self):
        return '<Song %s>' % self.spot_id
