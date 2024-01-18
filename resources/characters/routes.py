from flask import request
from uuid import uuid4
from flask.views import MethodView

from schemas import charactersSchema
from . import bp 
from db import characters, users
# character routes

@bp.route('/<character_id>')
class character(MethodView,):

    @bp.response(200, charactersSchema)
    def get(self, character_id):
        try:
            return {'character': characters[character_id]}, 200
        except KeyError:
            return {'message': "Invalid character"}, 400

    @bp.arguments(charactersSchema)
    def put(self, characters_data, character_id):
        try:
            character = characters[character_id]
            characters_data = request.get_json()
            if characters_data['user_id'] == character['user_id']:
                characters['power'] = characters_data['power']
                return { 'message': 'Character Updated'}, 202
            return {'message': "Unauthorized"}, 401
        except:
            return {'message': "Invalid Character Id"}, 400

    def delete(self, character_id):
        try:
            del characters[character_id]
            return {'message': "Character Deleted"}, 201
        except:
            return {'message': "Invalid Character"}, 400
    

@bp.route('/')
class character_list(MethodView):


    @bp.response(200, charactersSchema (many = True))
    def get(self):
        return list(characters.values())

    bp.arguments(charactersSchema)
    def post(self, character_data):
        character_data = request.get_json()
        user_id = character_data['user_id']
        if user_id in users:
            characters[uuid4()] = character_data
            return { 'message': "Character created" }, 201
        return { 'message': "Invalid user"}, 401

# @bp.get('/')
# def add_character():
#     return{'characters': list(characters.values())}

# @bp.get('/<character_id>')
# def get_character(character_id):
#     try:
#         return {'character': characters[character_id]}, 200
#     except KeyError:
#         return {'message': "Invalid character"}, 400

# @bp.post('/')
# def create_character():
#     character_data = request.get_json()
#     characters[uuid4] = character_data
#     user_id = character_data['user_id']
#     if user_id in users:
#         characters[uuid4()] = character_data
#         return { 'message': "Character created" }, 201
#     return { 'message': "Invalid user"}, 401

# @bp.put('/<character_id>')
# def update_character(character_id):
#     try:
#         character = characters[character_id]
#         characters_data = request.get_json()
#         if characters_data['user_id'] == character['user_id']:
#             characters['power'] = characters_data['power']
#             return { 'message': 'Character Updated'}, 202
#         return {'message': "Unauthorized"}, 401
#     except:
#         return {'message': "Invalid Character Id"}, 400

# @bp.delete('/<character_id>')
# def delete_character(character_id):
#     try:
#         del characters[character_id]
#         return {'message': "Character Deleted"}, 201
#     except:
#        return {'message': "Invalid Character"}, 400
    