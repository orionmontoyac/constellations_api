from http import HTTPStatus
from flask import jsonify, Blueprint


errors_v1_bp = Blueprint('errors', __name__)


# Exceptions
class ObjectNotFound(Exception):
    status_code = 404

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


class BadInputModel(TypeError):
    status_code = 400

    def __init__(self, message, errors):
        Exception.__init__(self)
        self.message = message
        self.errors = errors


# Handlers
@errors_v1_bp.app_errorhandler(404)
def invalid_route(e):
    response = {
        'message': "Invalid route.",
        'error': e.description
    }

    return jsonify(response), HTTPStatus.NOT_FOUND


@errors_v1_bp.app_errorhandler(ObjectNotFound)
def not_found(error):
    response = {
        'message': error.message,
        'error': "Not found."
    }

    return jsonify(response), error.status_code


@errors_v1_bp.app_errorhandler(BadInputModel)
def bad_input(error):
    response = {
        "message": error.message,
        "error": error.errors.__str__()
    }

    return jsonify(response), error.status_code
