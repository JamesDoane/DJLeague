# THE FLASK APP THAT WILL RUN THE WEBSITE.
from flask import *
from jinja2 import StrictUndefined
from sqlalchemy.sql import base
from sqlalchemy.sql.expression import func
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pytz
import requests

app = Flask(__name__)

connect_to_db(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# enables Flask sessions
app.secret_key = 'kdjfj#WK$JLKF8dsfslkdjf3fsnajcb%^#4w87SehR&Y#&RIRHbuSeufu9&Y&O#TR'
api_token = ""
app.jinja_env.undefined = StrictUndefined
app.add_url_rule(
    "/download_resume/<filename>", endpoint="download_file", build_only=True
)



@app.route('/')
def homepage():
    return render_template('homepage.html')
#routes to profile things
#_________________________
@app.route('/myprofile')
def logged_in_player_profile():
    return render_template('profile.html')

@app.route('/profile/<username>')
def player_profile(username):
    return render_template('profile.html',user_id=user_id)

@app.route('/editprofile')
def edit_profile():
    return render_template('edit_profile.html')


#routes to tournaments/tournament listings.
#__________________________________________
@app.route('/tournaments')
def tournament_listing():
    return render_template('tournament_listing.html')

#routes to sign-ups/payment/payout.
#__________________________________

@app.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')