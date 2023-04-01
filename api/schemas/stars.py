from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from api.models.stars import Stars
from api.api import db


class StarsSchema(SQLAlchemySchema):
    class Meta:
        model = Stars
        include_relationships = True
        sqla_session = db.session

    constellation_id = auto_field()
