from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy
db = SQLAlchemy()

class Database:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """ Initialize the app with the database """
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hbnb_evolution.db'  # Replace with your DB URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
    
    def create_all(self):
        """ Create all tables in the database """
        with app.app_context():
            db.create_all()

    def drop_all(self):
        """ Drop all tables from the database """
        with app.app_context():
            db.drop_all()

    def get_db_session(self):
        """ Get a new session for querying the database """
        return db.session

# You can also create some convenience functions for interacting with the database.

def create_session():
    """ Create a new session """
    return db.session()

def close_session(session):
    """ Close an active session """
    session.remove()

# Set up models in a similar way as done in models.py (example below)

# Example of a database model for a user
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<User {self.username}>"

# You would create similar models for City, Country, Review, Amenity, Place, etc.
