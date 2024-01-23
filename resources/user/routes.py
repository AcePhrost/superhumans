from flask import request


from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import abort
from . import bp

from schemas import userSchema,userSchemaNested
from models.user_model import UserModel

from resources import user
# user routes

@bp.route('/user/<user_id>')
class User(MethodView):

    @bp.response(200, userSchemaNested)
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if user:
            print(user.posts.all())
            return user
        else:
            abort(400, message='User not found')

@jwt_required()        
@bp.arguments(userSchema)
def put(self, user_data, user_id):
    user = UserModel.query.get(user_id)
    if user:
        user = UserModel.query.get(get_jwt_identity())
    if user and user.id == user_id:
        user.from_dict(user_data)
        user.commit()
        return { 'message': f'{user.username} updated'}, 202
    abort(400, message = "Invalid User")

def delete(self, user_id):
    user = UserModel.query.get(get_jwt_identity())
    if user == user_id:
      user.delete()
      return { 'message': f'User: {user.username} Deleted' }, 202
    return {'message': "Invalid username"}, 400
        
@bp.route('/user/follow/<followed_id>')
class FollowUser(MethodView):
    @jwt_required()
    def character(self, followed_id):
        followed = UserModel.query.get(followed_id)
        follower =UserModel.query.get(get_jwt_identity())
        if follower and followed:
            follower.follow(followed)
            followed.commit()
            return {'message':'user followed'}
        else:
            return {'message':'invalid user'}, 400
    jwt_required()  
    def put(self, followed_id):
        followed = UserModel.query.get(followed_id)
        follower = UserModel.query.get(get_jwt_identity())
        if follower and followed:
            follower.unfollow(followed)
            followed.commit()
            return {'message':'user unfollowed'}
        else:
            return {'message':'invalid user'}, 400