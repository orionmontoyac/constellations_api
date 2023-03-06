from datetime import datetime

from http import HTTPStatus
from flask import Blueprint
from flask_restful import Api, Resource

health_v1_bp = Blueprint('health_v1_bp', __name__)
api = Api(health_v1_bp)


class HealthCheck(Resource):
    @staticmethod
    def get():
        """
        Health check of the Constellations API.
        """
        return "Constellations API is Healthy. Date: {}".format(datetime.now()), HTTPStatus.OK


api.add_resource(HealthCheck, '/api/v1/health',
                 endpoint='health')
