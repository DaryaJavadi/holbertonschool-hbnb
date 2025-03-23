class BaseModel:
    """
    A base class for all models. It provides common attributes such as id and 
    methods for initializing the object.
    """
    def __init__(self, id=None):
        self.id = id


class User(BaseModel):
    def __init__(self, id=None, username="", email="", password=""):
        super().__init__(id)
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"


class Place(BaseModel):
    def __init__(self, id=None, name="", description="", city_id=None, user_id=None):
        super().__init__(id)
        self.name = name
        self.description = description
        self.city_id = city_id
        self.user_id = user_id

    def __repr__(self):
        return f"<Place(id={self.id}, name={self.name}, description={self.description})>"


class Review(BaseModel):
    def __init__(self, id=None, place_id=None, user_id=None, content="", rating=0):
        super().__init__(id)
        self.place_id = place_id
        self.user_id = user_id
        self.content = content
        self.rating = rating

    def __repr__(self):
        return f"<Review(id={self.id}, place_id={self.place_id}, user_id={self.user_id}, rating={self.rating})>"


class Amenity(BaseModel):
    def __init__(self, id=None, name="", place_id=None):
        super().__init__(id)
        self.name = name
        self.place_id = place_id

    def __repr__(self):
        return f"<Amenity(id={self.id}, name={self.name}, place_id={self.place_id})>"


class City(BaseModel):
    def __init__(self, id=None, name="", country_id=None):
        super().__init__(id)
        self.name = name
        self.country_id = country_id

    def __repr__(self):
        return f"<City(id={self.id}, name={self.name}, country_id={self.country_id})>"


class Country(BaseModel):
    def __init__(self, id=None, name=""):
        super().__init__(id)
        self.name = name

    def __repr__(self):
        return f"<Country(id={self.id}, name={self.name})>"
