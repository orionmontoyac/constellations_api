from http import HTTPStatus
from flask import Blueprint
from flask_restful import Api, Resource

home_v1_bp = Blueprint('api', __name__)
api = Api(home_v1_bp)


class Home(Resource):
    @staticmethod
    def get():
        """
        Home endpoint of Constellation API.
        """
        return "Wellcome to constellation API.", HTTPStatus.OK


api.add_resource(Home, '/api/v1/',
                 endpoint='home')
