from flask import request, Blueprint
from flask_restful import Api, Resource
from werkzeug.exceptions import BadRequest
from .schemas import ConstellationSchema
from ..models import Constellation, Star
from app.common.error_handling import InvalidToken

# from ...ext import ObjectNotFound

constellations_v1_0_bp = Blueprint('constellations_v1_0_bp', __name__)

constellation_schema = ConstellationSchema()

api = Api(constellations_v1_0_bp)

class ConstellationListResource(Resource):
    def get(self):
        constellations = Constellation.get_all()
        result = constellation_schema.dump(constellations, many=True)
        return result

    def post(self):
        auth = request.headers.get("X-Api-Key")
        if auth != "12345":
            raise InvalidToken("API KEY no valid")
        
        data = request.get_json()
        
        constellation_dict = constellation_schema.load(data)
        constellation = Constellation(name=constellation_dict['name'],
                                      abbr=constellation_dict['abbr'],
                                      english_name=constellation_dict['english_name'],
                                      pronunciation=constellation_dict['pronunciation']
                                      )
        
        for star in constellation_dict['stars']:
            constellation.stars.append(Star(star['name'],star['bayer_designation'], star["right_ascension"], star["declination"], star["apparent_magnitude"], star["absolute_magnitude"], star['distance']))
        constellation.save()

        resp = constellation_schema.dump(constellation)
        return resp, 201

class ConstellationResource(Resource):
    def get(self, constellation_id):
        constellation = Constellation.get_by_id(constellation_id)
        if constellation is None:
            return {"ERROR": "Constellation id no valid"}#raise #ObjectNotFound('La constelacion no existe')
        resp = constellation_schema.dump(constellation)
        return resp

api.add_resource(ConstellationListResource, '/api/v1.0/constellations/',
                 endpoint='constellation_list_resource')

api.add_resource(ConstellationResource, '/api/v1.0/constellations/<int:constellation_id>',
                 endpoint='constellation_resource')

