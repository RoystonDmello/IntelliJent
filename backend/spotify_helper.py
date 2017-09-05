from backend import spotify

def get_song(meta_dict):

    song = meta_dict['song'] 
    artist = meta_dict['artist']
    album = meta_dict['album']

    query = "track:" + song + " artist:" + artist + " album:" + album

    results = spotify.search(q=query, type="track", limit=1)

    return results['tracks']['items'][0]['id']

def get_features(spot_id):

    results = spotify.audio_features([spot_id])

    return results