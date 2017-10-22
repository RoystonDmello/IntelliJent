""" Collection of functions to get data from spotify API using the spotipy wrapper
"""

from backend import spotify


def get_song(meta_dict):

    song = meta_dict['Title']
    artist = meta_dict['Artist']
    album = meta_dict['Album']

    query = "track:" + song 

    if artist:
    	query = query + " artist:" + artist

    if album:
    	query = query + " album:" + album

    results = spotify.search(q=query, type="track", limit=1)

    return results['tracks']['items'][0]['id']

def get_features(spot_id):

    results = spotify.audio_features([spot_id])

    return results[0]

def get_songs(spot_ids):

    songs = spotify.tracks(spot_ids)

    sendable_songs = []
    # print songs
    for song in songs['tracks']:
    	# print song
    	sendable_song = {
    		"Artist": song['artists'][0]['name'],
    		"Album": song['album']['name'],
    		"Title": song['name']
    	}

    	sendable_songs.append(sendable_song)

    return {
    	"Songs": sendable_songs
    }	


    
