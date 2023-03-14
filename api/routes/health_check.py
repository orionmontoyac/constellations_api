from datetime import datetime

from http import HTTPStatus
from flask import Blueprint
from flask_restful import Api, Resource
from flasgger import swag_from

import api.utils.swagger.swagger_docs as swagger_docs

health_v1_bp = Blueprint('health_v1_bp', __name__)
api = Api(health_v1_bp)


class HealthCheck(Resource):
    @staticmethod
    @swag_from(swagger_docs.HEALTH_CHECK_GET_DOCS)
    def get():
        """
        Health check of the Constellations API.
        """
        return "Constellations API is Healthy. Date: {}".format(datetime.now()), HTTPStatus.OK


api.add_resource(HealthCheck, '/api/v1/health',
                 endpoint='health')
