from typing_extensions import Required
from . import db
from . import config
import base64


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

