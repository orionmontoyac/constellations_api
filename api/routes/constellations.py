from http import HTTPStatus
from flask import request, Blueprint, jsonify
from flask_restful import Api, Resource

from api.utils.database import Constellation
from api.schemas.schemas import ConstellationSchema

constellations_v1_bp = Blueprint('constellations_v1_bp', __name__)
api = Api(constellations_v1_bp)

# Set schemas
constellations_schema = ConstellationSchema()


class ConstellationList(Resource):
    @staticmethod
    def get():
        """
        GET all constellations.
        RETURN List of Constellations List[Constellation]
        """
        constellations = Constellation.get_all_constellations()
        return constellations_schema.dump(constellations, many=True), 200

    @staticmethod
    def post():
        """
        POST add 1 or more constellations.
        BODY List of Constellations List[Constellation]
        """
        data = request.get_json()
        for constellation_raw in data:
            # Check constellation model
            constellation = Constellation(**constellation_raw)
            # Save constellation to DB
            constellation.save()

        return "Constellation(s) saved", HTTPStatus.CREATED


class GetConstellation(Resource):
    @staticmethod
    def get(constellation_id: int):
        constellation = Constellation.query.get(constellation_id)
        print(constellation)
        return "One Constellation", HTTPStatus.OK


api.add_resource(ConstellationList, '/api/v1/constellations',
                 endpoint='constellation_list')
api.add_resource(GetConstellation, '/api/v1/constellation/<int:constellation_id>',
                 endpoint='get_constellation')
