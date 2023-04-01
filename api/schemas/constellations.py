from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from api.models.constellations import Constellations
from api.api import db


class ConstellationsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Constellations
        include_relationships = True
        load_instance = True
        sqla_session = db.session
