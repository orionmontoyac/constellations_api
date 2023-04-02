from api.utils.extensions import ma

from api.models.stars import Stars
from api.api import db


class StarsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Stars
        include_relationships = True
        load_instance = True
        sqla_session = db.session
        fields = ('name', 'id')
