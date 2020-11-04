from marshmallow import fields

from app.ext import ma


class ConstellationSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    abbr = fields.String(required=True)
    english_name = fields.String(required=True)
    pronunciation = fields.String(required=True)
    stars = fields.Nested('StarSchema', many=True)


class StarSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    bayer_designation = fields.String()
    right_ascension = fields.String()
    declination = fields.String()
    apparent_magnitude = fields.String()
    absolute_magnitude = fields.String()
    distance = fields.String()
