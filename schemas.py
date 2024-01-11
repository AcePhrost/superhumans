from marshmallow import Schema, fields

class users(Schema):
    id = fields.Str(dump_only = True)
    email = fields.Str(required = True)
    username = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True)
    first_name = fields.str()
    last_name = fields.Str()

class characters(Schema):
    id = fields.str(dump_only = True)
    attributes = fields.str(required = True)
    disadvantages = fields.str(required = True)