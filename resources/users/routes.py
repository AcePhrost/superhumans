from uuid import uuid4
from flask import request

from . import bp
from db import users

from schemas import usersSchema
# user routes


@bp.get('/user')
def user():
    return {'users': list(users.values())}, 200

@bp.get('/user/<user_id>')
@bp.response(201, usersSchema, many= True)
def get_user(user_id):
    try:
        return { 'user': users[user_id]}
    except:
        return {'message': "Invalid user"}, 400

@bp.post('/user')
@bp.arguments(usersSchema)
def create_user(user_data):
    users[uuid4()] = user_data
    return { 'message' : f'{user_data["username"]} created' }, 201
    
   

@bp.put('/user/<user_id>')
def update_user(user_id):
    try:
        user = users[user_id]
        user_data = request.get_json()
        user |= user_data
        return { 'message': f'{user["username"]} Updated'}, 202
    except KeyError:
        return {'message': "Invalid user"}, 400
    

@bp.delete('/user/<user_id>')
def delete_user(user_id):
    # user_data = request.get_json()
    # username = user_data['username']
    try: 
        del users[user_id]
        return {' message': f'User Deleted'}, 202
    except:
        return {'message': "Invalid Username"}, 400