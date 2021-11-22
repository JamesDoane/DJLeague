from flask_sqlalchemy import *
from sqlalchemy.orm import backref
import os

db = SQLAlchemy()





def connect_to_db(app):
    db.app = app
    db.init_app(app)
    uri = os.environ.get('DATABASE_URL')
    app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://")
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False