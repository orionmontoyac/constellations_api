from http import HTTPStatus
from flask import Blueprint
from flask_restful import Api, Resource

from api.utils.database import ConstellationModel
from api.utils.database import StarModel
from api.schemas.schemas import StarSchema
from api.utils.error_handling import ObjectNotFound

stars_v1_bp = Blueprint('stars_v1_bp', __name__)
api = Api(stars_v1_bp)

stars_schema = StarSchema()


class StarList(Resource):
    @staticmethod
    def get(constellation_id: int):
        """
        GET all stars from a constellation by id
        RETURN list of stars List[StarModel]
        """
        # Get constellation
        constellation = ConstellationModel.query.get(constellation_id)
        if constellation is None:
            raise ObjectNotFound("Constellations with id {} not found.".format(constellation_id))
        # Get stars
        stars = constellation.stars

        return stars_schema.dump(stars, many=True), HTTPStatus.OK


class Star(Resource):
    @staticmethod
    def get(constellation_id: int, star_id: int):
        """
        GET one single star from a constellation
        RETURN one single star StarModel
        """
        # Get constellation
        star = StarModel.query.filter_by(
            constellation_id=constellation_id,
            id=star_id
        ).first()

        if star is None:
            raise ObjectNotFound(
                "Start with id {} in constellations with id {} not found.".format(star_id, constellation_id))

        return stars_schema.dump(star, many=False), HTTPStatus.OK


api.add_resource(StarList, '/api/v1/constellation/<int:constellation_id>/stars',
                 endpoint='star_list')
api.add_resource(Star, '/api/v1/constellation/<int:constellation_id>/stars/<int:star_id>',
                 endpoint='star')
