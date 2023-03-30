from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from flask_restful import Api, Resource

from api.utils.swagger.swagger_docs import HOME_GET_DOCS

home_v1_bp = Blueprint("home_v1_bp", __name__)
api = Api(home_v1_bp)


class Home(Resource):
    @staticmethod
    @swag_from(HOME_GET_DOCS)
    def get():
        """
        Home endpoint of Constellation API.
        """
        return "Wellcome to constellation API. Version: 1.0", HTTPStatus.OK


api.add_resource(Home, "/api/v1/", endpoint="home")
