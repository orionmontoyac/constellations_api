from api.api import db
from api.models.constellations import Constellations


def get_all():
    return Constellations.query.order_by('name').all()


def create(constellations: dict) -> list:
    db.session.add(constellations)
    db.session.commit()
