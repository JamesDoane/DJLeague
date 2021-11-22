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
    return render_template('myprofile.html')

@app.route('/profile/<username>')
def player_profile(username):
    user = Player.query.first(id = session['logged_in_user_id'])
    return render_template('player_profile.html',user_id=user.id)

@app.route('/editprofile')
def edit_profile():
    return render_template('edit_profile.html')


#routes to tournaments/tournament listings.
#__________________________________________
@app.route('/tournaments')
def tournament_listing():
    return render_template('tournament_listing.html')

@app.route('/tournaments/<tournament_id>')
def tournament(tournament_id):
    return render_template('tournament_page.html')

@app.route('tournaments/<tournament_id>/sign_up')
def tournament_sign_up(tournament_id):
    return render_template('tournament_sign_up.html',tournament_id=tournament_id)

#routes to sign-ups/payment/payout.
#__________________________________

@app.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/login_page')
def login_page():
    return render_template('login_page.html')

@app.route('/login')
def login():
    flash("Login successful.")
    return redirect('/myprofile')

#admin routes, must be logged into administrator account to access.
#__________________________________________________________________

@app.route('/create_tournament')
def create_tournament():
    return render_template('create_tournament.html')

@app.route('/view_analytics')
def view_analytics():
    return render_template('analytics.html')