from flask import request, Blueprint
from flask_restful import Api, Resource
from werkzeug.exceptions import BadRequest
from .schemas import ConstellationSchema, StarSchema
from ..models import Constellation, Star
from app.common.error_handling import InvalidToken, ObjectNotFound

# from ...ext import ObjectNotFound

constellations_v1_0_bp = Blueprint('constellations_v1_0_bp', __name__)

constellation_schema = ConstellationSchema()
star_schema = StarSchema()

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
        
        query_parameters = request.args

        if constellation is None:
            return {"ERROR": "Constellation id no valid"}#raise #ObjectNotFound('La constelacion no existe')
        
        if query_parameters.get('star') != None:
            star_id = query_parameters.get('star')
            try:
                star = constellation.stars[int(star_id)]   
                return star_schema.dump(star)
            except IndexError:
                raise ObjectNotFound("Star {} in Constellation {} not found".format(star_id,constellation))
            except ValueError:
                raise ObjectNotFound("Star id '{}' is not a integer".format(star_id))
        
        resp = constellation_schema.dump(constellation)
        return resp

api.add_resource(ConstellationListResource, '/api/v1.0/constellations/',
                 endpoint='constellation_list_resource')

api.add_resource(ConstellationResource, '/api/v1.0/constellations/<int:constellation_id>',
                 endpoint='constellation_resource')
