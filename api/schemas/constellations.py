from extensions import ma

from api.models.constellations import Constellations
from api.schemas.stars import StarsSchema
from api.api import db


class ConstellationsSchema(ma.SQLAlchemyAutoSchema):
    stars = ma.Nested(StarsSchema, many=True)

    class Meta:
        model = Constellations
        include_relationships = True
        load_instance = True
        sqla_session = db.session
