from app.db import db, BaseModelMixin


class Constellation(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    abbr = db.Column(db.String)
    english_name = db.Column(db.String)
    pronunciation = db.Column(db.String)
    stars = db.relationship('Star', backref='constellation', lazy=False, cascade='all, delete-orphan')

    def __init__(self, name, abbr, english_name, pronunciation, stars=[]):
        self.name = name
        self.abbr = abbr
        self.english_name = english_name
        self.pronunciation = pronunciation
        self.stars = stars

    def __repr__(self):
        return f'Film({self.name})'

    def __str__(self):
        return f'{self.name}'


class Star(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bayer_designation = db.Column(db.String)
    right_ascension = db.Column(db.String)
    declination = db.Column(db.String)
    apparent_magnitude = db.Column(db.String)
    absolute_magnitude = db.Column(db.String)
    distance = db.Column(db.String)
    constellation_id = db.Column(db.Integer, db.ForeignKey('constellation.id'), nullable=False)

    def __init__(self, name, bayer_designation, right_ascension, declination, apparent_magnitude, absolute_magnitude, distance):
        self.name = name
        self.bayer_designation = bayer_designation
        self.right_ascension = right_ascension
        self.declination = declination
        self.apparent_magnitude = apparent_magnitude
        self.absolute_magnitude = absolute_magnitude
        self.distance = distance

    def __repr__(self):
        return f'Star({self.name})'

    def __str__(self):
        return f'{self.name}'
