from http import HTTPStatus
from flask import request, Blueprint
from flask_restful import Api, Resource
from flasgger import swag_from
from marshmallow import ValidationError

from api.api import db
from api.schemas.constellations import ConstellationsSchema
from api.utils.error_handling import ObjectNotFound, BadInputModel
import api.utils.swagger.swagger_docs as swagger_docs
import api.controllers.constellations as constellations_controller


constellations_v1_bp = Blueprint("constellations_v1_bp", __name__)
api = Api(constellations_v1_bp)


class ConstellationList(Resource):
    @staticmethod
    @swag_from(swagger_docs.CONSTELLATIONS_LIST_GET_DOCS)
    def get():
        """
        GET all constellations.
        RETURN List of Constellations List[ConstellationModel]
        """
        constellations_schema = ConstellationsSchema()

        constellations = constellations_controller.get_all()
        response = constellations_schema.jsonify(constellations, many=True)
        response.status_code = HTTPStatus.OK

        return response

    @staticmethod
    @swag_from(swagger_docs.CONSTELLATIONS_LIST_POST_DOCS)
    def post():
        """
        POST add 1 or more constellations.
        BODY List of Constellations List[ConstellationModel]
        """
        constellations_schema = ConstellationsSchema()
        data = request.json

        if not data:
            return "json parameter is required", HTTPStatus.BAD_REQUEST

        for constellation_raw in data:
            # Check constellation model
            try:
                constellation = constellations_schema.load(constellation_raw, session=db.session)
            except ValidationError as e:
                raise BadInputModel(message="Input validation error.", errors=e)

            # Save constellation to DB
            constellations_controller.create(constellation)

        return 'Constellation(s) saved', HTTPStatus.CREATED


class Constellation(Resource):
    @staticmethod
    @swag_from(swagger_docs.CONSTELLATION_GET_DOCS)
    def get(constellation_id: int):
        """
        GET on constellation by id number
        RETURN one single constellation ConstellationModel
        """
        constellation = constellations_controller.get_one(constellation_id)

        if constellation is None:
            raise ObjectNotFound(
                "Constellations with id {} not found.".format(constellation_id)
            )

        constellations_schema = ConstellationsSchema()

        response = constellations_schema.jsonify(constellation)
        response.status_code = HTTPStatus.OK

        return response

    @staticmethod
    @swag_from(swagger_docs.CONSTELLATION_PUT_DOCS)
    def put(constellation_id):
        """
        UPDATE one single constellation by id number
        BODY one constellation ConstellationModel
        """
        # Check if constellations exits
        current_constellation = constellations_controller.get_one(constellation_id)
        if current_constellation is None:
            raise ObjectNotFound(
                "Constellations with id {} not found.".format(constellation_id)
            )

        constellations_schema = ConstellationsSchema()
        data = request.json
        # Check constellation model
        try:
            update_constellation = constellations_schema.load(
                data, session=db.session, instance=current_constellation, partial=True)
        except ValidationError as e:
            raise BadInputModel(message="Input validation error.", errors=e)

        # Update constellation
        constellations_controller.update()

        response = constellations_schema.jsonify(update_constellation)
        response.status_code = HTTPStatus.OK

        return response

    @staticmethod
    @swag_from(swagger_docs.CONSTELLATION_DELETE_DOCS)
    def delete(constellation_id):
        """
        DELETE on single constellation by id
        """
        # Check if constellations exits
        current_constellation = constellations_controller.get_one(constellation_id)
        if current_constellation is None:
            raise ObjectNotFound(
                "Constellations with id {} not found.".format(constellation_id)
            )

        # Delete constellation
        constellations_controller.delete(current_constellation)

        return "Constellation deleted", HTTPStatus.OK


api.add_resource(
    ConstellationList, "/api/v1/constellations", endpoint="constellation_list"
)
api.add_resource(
    Constellation,
    "/api/v1/constellation/<int:constellation_id>",
    endpoint="get_constellation",
)
