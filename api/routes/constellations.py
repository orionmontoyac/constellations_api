from http import HTTPStatus
from flask import request, Blueprint
from flask_restful import Api, Resource

from api.utils.database import ConstellationModel
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
        RETURN List of Constellations List[ConstellationModel]
        """
        constellations = ConstellationModel.get_all_constellations()
        return constellations_schema.dump(constellations, many=True), HTTPStatus.OK

    @staticmethod
    def post():
        """
        POST add 1 or more constellations.
        BODY List of Constellations List[ConstellationModel]
        """
        data = request.get_json()
        for constellation_raw in data:
            # Check constellation model
            constellation = ConstellationModel(**constellation_raw)
            # Save constellation to DB
            constellation.save()

        return "Constellation(s) saved", HTTPStatus.CREATED


class Constellation(Resource):
    @staticmethod
    def get(constellation_id: int):
        """
        GET on constellation by id number
        RETURN one single constellation ConstellationModel
        """
        # Get constellation
        constellation = ConstellationModel.query.get(constellation_id)
        if constellation is None:
            return "Constellation not found.", HTTPStatus.NOT_FOUND

        return constellations_schema.dump(constellation), HTTPStatus.OK

    @staticmethod
    def put(constellation_id):
        """
        UPDATE one single constellation by id number
        BODY one constellation ConstellationModel
        """
        data = request.get_json()
        # Check constellation model
        constellation = ConstellationModel(**data)
        # Update constellation
        constellation_updated = constellation.update(constellation_id, data)

        return constellations_schema.dump(constellation_updated), HTTPStatus.OK

    @staticmethod
    def delete(constellation_id):
        """
        DELETE on single constellation by id
        """
        # Get constellation
        constellation = ConstellationModel.query.get(constellation_id)
        if constellation is None:
            return "Constellation not found.", HTTPStatus.NOT_FOUND

        # Delete constellation
        constellation.delete(constellation_id)

        return "Constellation deleted", HTTPStatus.OK


api.add_resource(ConstellationList, '/api/v1/constellations',
                 endpoint='constellation_list')
api.add_resource(Constellation, '/api/v1/constellation/<int:constellation_id>',
                 endpoint='get_constellation')
