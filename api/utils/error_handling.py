from http import HTTPStatus
from flask import jsonify, Blueprint

errors_v1_bp = Blueprint('errors', __name__)


# Exceptions
class ObjectNotFound(Exception):
    status_code = 404

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


# Handlers
@errors_v1_bp.app_errorhandler(ObjectNotFound)
def not_found(error):
    response = {
        'message': error.message
    }

    return jsonify(response), error.status_code
