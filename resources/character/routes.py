from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import characterModel
from schemas import characterSchema, characterSchemaNested

from . import bp
# character routes

@bp.route('/<character_id>')
class character(MethodView,):

    @bp.response(200, characterSchemaNested)
    def get(self, character_id):
        character = characterModel.query.get(character_id)
        if character:
            return character
        abort(400, message='Invalid character')

    @jwt_required
    @bp.arguments(characterSchema)
    def put(self, character_data, character_id):
        character = characterModel.query.get(character_id)
        if character and character.user_id == get_jwt_identity():
            character.power = character_data['power']
            character.commit()
            return {'message': 'character updated'}, 201
        return {'message': "Invalid Character Id"}, 400

    @jwt_required()
    def delete(self, character_id):
        character = characterModel.query.get(character_id)
        if character and character.user_id == get_jwt_identity():
            character.delete()
            return {"message": "Post Deleted"}, 202
        return {'message':"Invalid Character or User"}, 400

    @bp.route('/')
    class CharacterList(MethodView):

        @bp.response(200, characterSchema (many = True))
        def get(self):
            return characterModel.query.all()
        
        @jwt_required()
        @bp.arguments(characterSchema)
        def character(self, character_data):
            try:
                character = characterModel
                character.user_id = get_jwt_identity()
                character.power = character_data['power']
                character.commit()
                return { 'message': "Character created" }, 201
            except:
                return { 'message': "Invalid user"}, 401
       
