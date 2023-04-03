from api.utils.extensions import db
from api.models.constellations import Constellations


def get_all():
    response = Constellations.query.all()
    return response


def get_one(constellations_id: int):
    response = Constellations.query.get(constellations_id)
    return response


def create(constellations: dict):
    db.session.add(constellations)
    db.session.commit()


def update():
    db.session.commit()


def delete(constellation: Constellations):
    db.session.delete(constellation)
    db.session.commit()
