from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

users = {
    '1' : {
        'username': 'Phrosty',
        'email': 'cam@mail.com'
    },
    '2': {
        'username': 'CamO',
        'email': 'O@mail.com'
    }
}

characters = {
    '1' : {
        'power': 'Jack Frost Ice',
        'user_id': '1'
    },
    '2': {
        'power': 'Shadow Manipulation',
        'user_id': '2'
    }
}

# user routes
@app.get('/user')
def user():
    return {'users': list(users.values())}, 200

@app.post('/user')
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return { 'message' : f'{json_body["username"]} created' }, 201

@app.put('/user/<user_id>')
def update_user(user_id):
    try:
        user = users[user_id]
        user_data = request.get_json()
        user |= user_data
        return { 'message': f'{user["username"]} Updated'}, 202
    except KeyError:
        return {'message': "Invalid user"}, 400
    

@app.delete('/user/<user_id>')
def delete_user(user_id):
    # user_data = request.get_json()
    # username = user_data['username']
    try: 
        del users[user_id]
        return {' message': f'User Deleted'}, 202
    except:
        return {'message': "Invalid Username"}, 400
 


# character routes

@app.get('/characters')
def add_character():
    return{'characters': list(characters.values())}

@app.post('/characters')
def create_character():
    character_data = request.get_json()
    characters[uuid4] = character_data
    user_id = character_data['user_id']
    if user_id in users:
        characters[uuid4()] = character_data
        return { 'message': "Character created" }, 201
    return { 'message': "Invalid user"}, 401

@app.put('/characters')
def update_character():
    return

@app.delete('/characters')
def delete_character():
    return