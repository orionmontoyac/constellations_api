from http import HTTPStatus
from flask import Blueprint

home_api = Blueprint('api', __name__)


@home_api.route('/')
def welcome():
    """
    Home endpoint of Constellation API.
    """
    return "Wellcome to constellation API.", HTTPStatus.OK
