from uuid import uuid4
from flask import request
from flask.views import MethodView

from . import bp
from db import users

from schemas import usersSchema
# user routes

@bp.route('/user/<user_id>')
class User(MethodView):

    @bp.response(200, usersSchema)
    def get(self, user_id):
        try:
            return users[user_id]
        except:
            return {'message': "Invalid user"}, 400
    
    @bp.arguments(usersSchema)
    def put(self, user_data, user_id):
        try:
            user = users[user_id]
            user_data = request.get_json()
            user |= user_data
            return { 'message': f'{user["username"]} Updated'}, 202
        except KeyError:
            return {'message': "Invalid user"}, 400

    def delete(self, user_id):
        try: 
            del users[user_id]
            return {' message': f'User Deleted'}, 202
        except:
            return {'message': "Invalid Username"}, 400
        
@bp.route('/user')
class userList(MethodView):

    @bp.response(200, usersSchema(many = True))
    def get(self):
        return list(users.values())
    
    @bp.arguments(usersSchema)
    def post(self, user_data):
        users[uuid4()] = user_data
        return { 'message' : f'{user_data["username"]} created' }, 201

