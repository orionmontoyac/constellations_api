from marshmallow import fields, Schema


class StarSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)


class ConstellationSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    abbr = fields.String(required=True)
    english_name = fields.String(required=True)
    stars = fields.Nested(StarSchema, many=True)

