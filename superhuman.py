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

@app.put('/user')
def update_user():
    return

@app.delete('user')
def delete_user():
    pass


# character routes

@app.get('/characters')
def add_character():
    return

@app.post('/characters')
def create_character():
    return

@app.put('/characters')
def update_character():
    return

@app.delete('/characters')
def delete_character():
    return