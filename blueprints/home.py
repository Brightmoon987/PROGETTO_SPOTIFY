from flask import Blueprint, session, redirect, url_for, render_template
import spotipy

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def homepage():
    token_info = session.get('token_info')
    if not token_info:
        return redirect(url_for('auth.login'))

    sp = spotipy.Spotify(auth=token_info['access_token'])
    user_info = sp.current_user()
    playlists = sp.current_user_playlists()['items']

    return render_template('home.html', user_info=user_info, playlists=playlists)





@home_bp.route('/playlist/<playlist_id>')
def playlist_tracks(playlist_id):
    token_info = session.get('token_info')
    if not token_info:
        return redirect(url_for('auth.login'))

    sp = spotipy.Spotify(auth=token_info['access_token'])
    playlist = sp.playlist_items(playlist_id, limit=100)

    tracks = [{'name': item['track']['name'],
               'artist': ', '.join([artist['name'] for artist in item['track']['artists']]),
               'album': item['track']['album']['name']} for item in playlist['items']]

    return render_template('playlist.html', tracks=tracks)