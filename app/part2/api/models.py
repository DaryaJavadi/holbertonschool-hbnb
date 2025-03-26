from flask_sqlalchemy import SQLAlchemy

# Initialize the db instance
db = SQLAlchemy()

class BaseModel:
    """
    A base class for all models. It provides common attributes such as id and 
    methods for initializing the object.
    """
    def __init__(self, id=None):
        self.id = id


class User(BaseModel, db.Model):  # Add db.Model here
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Add is_admin field here

    def __init__(self, id=None, username="", email="", first_name="", last_name="", password="", is_admin=False):
        super().__init__(id)
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, first_name={self.first_name}, last_name={self.last_name})>"

class Review(BaseModel, db.Model):  # Add db.Model here
    __tablename__ = 'reviews'  # You can specify the table name if needed

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to User
    content = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, id=None, place_id=None, user_id=None, content="", rating=0):
        super().__init__(id)
        self.place_id = place_id
        self.user_id = user_id
        self.content = content
        self.rating = rating

    def __repr__(self):
        return f"<Review(id={self.id}, place_id={self.place_id}, user_id={self.user_id}, rating={self.rating})>"


class Amenity(BaseModel, db.Model):  # Add db.Model here
    __tablename__ = 'amenities'  # You can specify the table name if needed

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    place_id = db.Column(db.Integer, nullable=False)

    def __init__(self, id=None, name="", place_id=None):
        super().__init__(id)
        self.name = name
        self.place_id = place_id

    def __repr__(self):
        return f"<Amenity(id={self.id}, name={self.name}, place_id={self.place_id})>"


class City(BaseModel, db.Model):  # Add db.Model here
    __tablename__ = 'cities'  # You can specify the table name if needed

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)  # Foreign key to Country

    def __init__(self, id=None, name="", country_id=None):
        super().__init__(id)
        self.name = name
        self.country_id = country_id

    def __repr__(self):
        return f"<City(id={self.id}, name={self.name}, country_id={self.country_id})>"


class Country(BaseModel, db.Model):  # Add db.Model here
    __tablename__ = 'countries'  # You can specify the table name if needed

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, id=None, name=""):
        super().__init__(id)
        self.name = name

    def __repr__(self):
        return f"<Country(id={self.id}, name={self.name})>"
