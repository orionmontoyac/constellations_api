from api.api import db
from api.models.constellations import Constellations


def get_all():
    response = Constellations.query.all()
    return response


def create(constellations: dict):
    db.session.add(constellations)
    db.session.commit()
