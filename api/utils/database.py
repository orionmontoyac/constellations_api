from typing import List, Dict
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Star(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    constellation_id = db.Column(db.Integer, db.ForeignKey('constellation.id'), nullable=False)

    def __init__(self, name: str):
        self.name = name


class Constellation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    abbr = db.Column(db.String, nullable=False)
    right_ascension = db.Column(db.String, nullable=False)
    stars = db.relationship('Star', backref='constellation', lazy=False, cascade='all, delete-orphan')

    def __init__(self, name: str, abbr: str, right_ascension: str, stars: List[Dict] = None):
        self.name = name
        self.abbr = abbr
        self.right_ascension = right_ascension
        self.stars = [Star(**star) for star in stars]

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_constellations(cls):
        # Get all constellation sorted by name
        constellations = cls.query.order_by(cls.name).all()

        return constellations

