from marshmallow import fields, Schema


class StarSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)


class ConstellationSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    abbr = fields.String(required=True)
    right_ascension = fields.String(required=True)
    stars = fields.Nested(StarSchema, many=True)
