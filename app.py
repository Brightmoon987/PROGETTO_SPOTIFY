from flask import Flask, redirect, request, url_for, render_template,session
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from blueprints.auth import auth_bp
from blueprints.home import home_bp




# client id: 794f04ed0af847559a4f79264ab0c369

# client secret; 5b24cedab54749979222a8906aca3b24



#le tue credenziali le trovi nella dashboard di prima
SPOTIFY_CLIENT_ID = "794f04ed0af847559a4f79264ab0c369"
SPOTIFY_CLIENT_SECRET = "5b24cedab54749979222a8906aca3b24"
SPOTIFY_REDIRECT_URI = "https://5000-brightmoon9-progettospo-onjjsgmrc18.ws-eu117.gitpod.io/callback" #dopo il login andiamo qui

app = Flask(__name__)
app.secret_key = 'chiave_per_session' #ci serve per identificare la sessione



app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)



#configurazione SpotifyOAuth per l'autenticazione e redirect uri

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private", #permessi x informazioni dell'utente
    show_dialog=True

)


@app.route('/')
def login():
    auth_url = sp_oauth.get_authorize_url() #login di spotify
    return redirect(auth_url)



@app.route('/callback')
def callback():
    code = request.args.get('code') #recupero codice di autorizzazione
    token_info = sp_oauth.get_access_token(code) #uso il code per un codice di accesso
    session['token_info'] = token_info #salvo il token nella mia sessione x riutilizzarlo
    return redirect(url_for('home'))





@app.route('/home')
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




@app.route('/logout')
def logout():
    session.clear() #cancelliamo l'access token salvato in session
    return redirect(url_for('login'))



@app.route('/playlist/<playlist_id>')
def playlist_tracks(playlist_id):
    token_info = session.get('token_info', None) #token sessione
    if not token_info:
        return redirect(url_for('login')) #ritorna la pagina del login.

    sp = spotipy.Spotify(auth=token_info['access_token'])
    playlist = sp.playlist_items(playlist_id, limit=100)  # Recuperiamo i brani

    tracks = []
    for item in playlist['items']: #per elemento in playlist aggiungi canzoni con esse i dati che devono essere aggiunte alla lista tracks
        track = item['track'] 
        tracks.append({
            'name': track['name'],
            'artist': ', '.join([artist['name'] for artist in track['artists']]), #per artista in canzone unisci il nome 
            'album': track['album']['name']
        })

    return render_template('playlist.html', tracks=tracks)


















































if __name__ == '__main__': #debug
    app.run(debug=True)























