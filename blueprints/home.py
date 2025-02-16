from flask import Blueprint, redirect, request, url_for, session
from services.spotify_oauth import sp_oauth, get_spotify_object


home_bp = Blueprint('home', __name__) #creiamo il blueprint


@home_bp.route('/home')
def home():
    token_info = session.get('token_info', None) #recupero token sissione (salvato prima)
    if not token_info:
        return redirect(url_for('login'))


    sp = spotipy.Spotify(auth=token_info['access_token']) #usiamo il token per ottenere i dati del profilo
    user_info = sp.current_user()
    playlists = sp.current_user_playlists() #sempre tramite il token sp preso prima
    playlists_info = playlists['items'] #prendiamo solo la lista delle playlist
    
    
    
    print(user_info) #capiamo la struttura di user_info per usarle nel frontend
    return render_template('home.html', user_info=user_info, playlists=playlists_info) #passo le info utente all'home.html