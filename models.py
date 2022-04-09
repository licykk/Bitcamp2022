from typing_extensions import Required
# from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager
from . import config
from .utils import current_time
import base64


# @login_manager.user_loader
# def load_user(user_id):
#     return User.objects(username=user_id).first()

# class User(db.Document, UserMixin):
#     username = db.StringField(required=True, unique=True)
#     email = db.EmailField(required=True, unique=True)
#     password = db.StringField(required=True)
#     profile_pic = db.ImageField()

#     # Returns unique string identifying our object
#     def get_id(self):
#         return self.username

class Task(db.EmbeddedDocument):
    name = db.StringField(required=True) #description/name"
    priority = db.StringField() #make an option
    assignment = db.StringField() #who is this task assigned to?
    due_date = db.StringField() #perhaps a date field? 
    status = db.StringField()

class File(db.EmbeddedDocument):
    name = db.StringField(required=True)
    file = db.StringField(required=True)
    
class Project(db.Document):
    # poster = db.ReferenceField(User, required=True)
    name = db.StringField(required=True)
    files = db.ListField(db.EmbeddedDocumentField(File))
    tasks = db.ListField(db.EmbeddedDocumentField(Task))

