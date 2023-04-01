from http import HTTPStatus
from flask import request, Blueprint
from flask_restful import Api, Resource
from flasgger import swag_from
from marshmallow import ValidationError

from api.api import db
from api.utils.database import ConstellationModel
from api.schemas.constellations import ConstellationsSchema
from api.utils.error_handling import ObjectNotFound, BadInputModel
import api.utils.swagger.swagger_docs as swagger_docs
import api.controllers.constellations as constellations_controller


constellations_v1_bp = Blueprint("constellations_v1_bp", __name__)
api = Api(constellations_v1_bp)

# Set schemas



class ConstellationList(Resource):
    @staticmethod
    @swag_from(swagger_docs.CONSTELLATIONS_LIST_GET_DOCS)
    def get():
        """
        GET all constellations.
        RETURN List of Constellations List[ConstellationModel]
        """
        constellations = constellations_controller.get_all()
        return constellations_schema.dump(constellations, many=True), HTTPStatus.OK

    @staticmethod
    @swag_from(swagger_docs.CONSTELLATIONS_LIST_POST_DOCS)
    def post():
        """
        POST add 1 or more constellations.
        BODY List of Constellations List[ConstellationModel]
        """
        constellations_schema = ConstellationsSchema()
        data = request.get_json()
        constellations_added = []
        for constellation_raw in data:
            # Check constellation model
            try:
                constellations = constellations_schema.load(constellation_raw, session=db.session)
            except ValidationError as e:
                raise BadInputModel(message="Input validation error.", errors=e)

            # Save constellation to DB
            constellations_added = constellations_controller.create(constellations)

        return constellations_added, HTTPStatus.CREATED


class Constellation(Resource):
    @staticmethod
    @swag_from(swagger_docs.CONSTELLATION_GET_DOCS)
    def get(constellation_id: int):
        """
        GET on constellation by id number
        RETURN one single constellation ConstellationModel
        """
        # Get constellation
        constellation = ConstellationModel.get_one_constellation(constellation_id)
        if constellation is None:
            raise ObjectNotFound(
                "Constellations with id {} not found.".format(constellation_id)
            )

        return constellations_schema.dump(constellation), HTTPStatus.OK

    @staticmethod
    @swag_from(swagger_docs.CONSTELLATION_PUT_DOCS)
    def put(constellation_id):
        """
        UPDATE one single constellation by id number
        BODY one constellation ConstellationModel
        """
        data = request.get_json()
        # Check constellation model
        try:
            ConstellationModel(**data)
        except TypeError as e:
            raise BadInputModel(message="Input validation error.", errors=e)

        # Get constellation
        constellation = ConstellationModel.get_one_constellation(constellation_id)
        if constellation is None:
            raise ObjectNotFound(
                "Constellations with id {} not found.".format(constellation_id)
            )

        # Update constellation
        constellation_updated = constellation.update(constellation, data)

        return constellations_schema.dump(constellation_updated), HTTPStatus.OK

    @staticmethod
    @swag_from(swagger_docs.CONSTELLATION_DELETE_DOCS)
    def delete(constellation_id):
        """
        DELETE on single constellation by id
        """
        # Get constellation
        constellation = ConstellationModel.get_one_constellation(constellation_id)
        if constellation is None:
            raise ObjectNotFound(
                "Constellations with id {} not found.".format(constellation_id)
            )

        # Delete constellation
        constellation.delete(constellation_id)

        return "Constellation deleted", HTTPStatus.OK


api.add_resource(
    ConstellationList, "/api/v1/constellations", endpoint="constellation_list"
)
api.add_resource(
    Constellation,
    "/api/v1/constellation/<int:constellation_id>",
    endpoint="get_constellation",
)
