from flask import Flask, redirect, request, url_for, render_template,session
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from blueprints.auth import auth_bp
from blueprints.home import home_bp





# client id: 794f04ed0af847559a4f79264ab0c369

# client secret; 5b24cedab54749979222a8906aca3b24



#le tue credenziali le trovi nella dashboard di prima

app = Flask(__name__)
app.secret_key = 'chiave_per_session' #ci serve per identificare la sessione



app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)



#configurazione SpotifyOAuth per l'autenticazione e redirect uri



if __name__ == '__main__': #debug
    app.run(debug=True)























