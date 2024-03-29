from http import HTTPStatus
from flask import Blueprint
from flask_restful import Api, Resource
from flasgger import swag_from

from api.schemas.stars import StarsSchema
import api.controllers.stars as stars_controller
from api.utils.error_handling import ObjectNotFound
import api.utils.swagger.swagger_docs as swagger_docs

stars_v1_bp = Blueprint("stars_v1_bp", __name__)
api = Api(stars_v1_bp)

stars_schema = StarsSchema()


class StarList(Resource):
    @staticmethod
    @swag_from(swagger_docs.STAR_LIST_GET_DOCS)
    def get(constellation_id: int):
        """
        GET all stars from a constellation by id
        RETURN list of stars List[StarModel]
        """

        stars_schema = StarsSchema()
        # Get stars
        stars = stars_controller.get_all(constellation_id)

        response = stars_schema.jsonify(stars, many=True)
        response.status_code = HTTPStatus.OK

        return response


class Star(Resource):
    @staticmethod
    @swag_from(swagger_docs.STAR_GET_DOCS)
    def get(constellation_id: int, star_id: int):
        """
        GET one single star from a constellation
        RETURN one single star StarModel
        """

        star = stars_controller.get_one(constellation_id, star_id)

        if star is None:
            raise ObjectNotFound(
                "Start with id {} in constellations with id {} not found.".format(
                    star_id, constellation_id
                )
            )

        stars_schema = StarsSchema()

        response = stars_schema.jsonify(star)
        response.status_code = HTTPStatus.OK

        return response


api.add_resource(
    StarList, "/api/v1/constellation/<int:constellation_id>/stars", endpoint="star_list"
)
api.add_resource(
    Star,
    "/api/v1/constellation/<int:constellation_id>/star/<int:star_id>",
    endpoint="star",
)
