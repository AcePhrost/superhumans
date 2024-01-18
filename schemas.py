from marshmallow import Schema, fields

class usersSchema(Schema):
    id = fields.Str(dump_only = True)
    email = fields.Str(required = True)
    username = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True)
    first_name = fields.Str()
    last_name = fields.Str()

class charactersSchema(Schema):
    id = fields.Str(dump_only = True)
    attributes = fields.Str(required = True)
    disadvantages = fields.Str(required = True)
    user_id = fields.Str(required = True)