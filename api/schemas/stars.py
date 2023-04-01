from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from api.models.stars import Stars


class StarsSchema(SQLAlchemySchema):
    class Meta:
        model = Stars
        include_relationships = True

    constellation_id = auto_field()
