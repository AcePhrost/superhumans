# from datetime import datetime

# from app import db


# class characterModels(db.Model):
    
#     __tablename__ = 'characters'

#     id = db.Column(db.Integer, primary_key = True)
#     power = db.Column(db.String, nullable = False)
#     timestamp = db.Column(db.String)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

#     def __repr__(self):
#         return f'<Post: {self.power}>'

#     def commit(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
