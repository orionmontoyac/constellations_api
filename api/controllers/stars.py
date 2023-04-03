from api.models.stars import Stars


def get_all(constellation_id):
    response = Stars.query.filter_by(
        constellation_id=constellation_id
    ).all()
    return response


def get_one(constellation_id: int, star_id: int) -> Stars:
    response = Stars.query.filter_by(
        constellation_id=constellation_id, id=star_id
    ).first()
    return response
