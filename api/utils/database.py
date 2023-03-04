from typing import List, Dict
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class StarModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    constellation_id = db.Column(db.Integer, db.ForeignKey('constellation_model.id'), nullable=False)

    def __init__(self, name: str):
        self.name = name


class ConstellationModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    abbr = db.Column(db.String, nullable=False)
    right_ascension = db.Column(db.String, nullable=False)
    stars = db.relationship('StarModel', backref='constellation_model', lazy=False, cascade='all, delete-orphan')

    def __init__(self, name: str, abbr: str, right_ascension: str, stars: List[Dict] = None):
        self.name = name
        self.abbr = abbr
        self.right_ascension = right_ascension
        self.stars = [StarModel(**star) for star in stars]

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def delete(constellation_id: int):
        constellation = db.session.query(ConstellationModel).filter(ConstellationModel.id == constellation_id).one()
        db.session.delete(constellation)
        db.session.commit()

    @staticmethod
    def update(constellation_id: int, constellation_update: Dict):
        constellation = db.session.query(ConstellationModel).filter(ConstellationModel.id == constellation_id).one()

        constellation.name = constellation_update["name"]
        constellation.abbr = constellation_update["abbr"]
        constellation.right_ascension = constellation_update["right_ascension"]
        constellation.stars = [StarModel(**star) for star in constellation_update["stars"]]

        db.session.commit()

        return constellation

    @classmethod
    def get_one_constellation(cls, constellation_id: int):
        # Get one constellation by id
        constellation = cls.query.filter_by(id=constellation_id).first()

        return constellation

    @classmethod
    def get_all_constellations(cls):
        # Get all constellations sorted by name
        constellations = cls.query.order_by(cls.name).all()

        return constellations
