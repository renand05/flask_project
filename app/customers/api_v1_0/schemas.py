from marshmallow import fields

from app.ext import ma


class CustomerSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String()
    last_name = fields.String()
    birth_date = fields.String()
    email = fields.String()
