from flask_sqlalchemy import *
from sqlalchemy.orm import backref
import os

db = SQLAlchemy()

class Player(db.Model):

    __tablename__ = 'players'


    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    email = db.Column(db.String(24), nullable=False)
    passhash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(48), nullable=True)
    last_name = db.Column(db.String(48), nullable=True)
    activision_id = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(128), nullable=True)
    last_30_day_kd = db.Column(db.Float)
    date_created = db.Column(db.DateTime)



class Duos(db.Model):

    __tablename__ = 'duos'

    

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_name = db.Column(db.String(24),nullable=False)
    player1_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    player2_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    team_kd = db.Column(db.Float)

    players = db.relationship("Player", backref=db.backref('duos', order_by=id))


class Trios(db.Model):

    __tablename__ = 'trios'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_name = db.Column(db.String(24),nullable=False)
    player1_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    player2_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    player3_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    team_kd = db.Column(db.Float)

    players = db.relationship("Player", backref=db.backref('trios', order_by=id))

class Quads(db.Model):

    __tablename__ = 'quads'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_name = db.Column(db.String(24),nullable=False)
    player1_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    player2_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    player3_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    player4_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    team_kd = db.Column(db.Float)

    players = db.relationship("Player", backref=db.backref("quads", order_by=id))

class Tournament(db.Model):

    __tablename__ = "tournaments"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_size = db.Column(db.Integer)
    buy_in = db.Column(db.String)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

def connect_to_db(app):
    db.app = app
    db.init_app(app)
    # uri = os.environ.get('DATABASE_URL')
    # app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')
    # if uri.startswith("postgres://"):
    #     uri = uri.replace("postgres://", "postgresql://")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Warzone'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
