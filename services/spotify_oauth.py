from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "794f04ed0af847559a4f79264ab0c369"
SPOTIFY_CLIENT_SECRET = "5b24cedab54749979222a8906aca3b24"
SPOTIFY_REDIRECT_URI = "https://5000-brightmoon9-progettospo-onjjsgmrc18.ws-eu117.gitpod.io/callback"

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private",
    show_dialog=True
)












