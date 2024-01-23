from marshmallow import Schema, fields

class userSchema(Schema):
    id = fields.Str(dump_only = True)
    email = fields.Str(required = True)
    username = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True)
    first_name = fields.Str()
    last_name = fields.Str()

class UserLogin(Schema):
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )

class characterSchema(Schema):
    id = fields.Str(dump_only = True)
    attributes = fields.Str(required = True)
    disadvantages = fields.Str(required = True)
    
class characterSchemaNested(characterSchema):
  user = fields.Nested(userSchema, dump_only = True)
  
class UserSchemaNested(userSchema):
  posts = fields.List(fields.Nested(characterSchema), dump_only=True)