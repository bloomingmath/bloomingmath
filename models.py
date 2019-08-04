from mongoengine import *
from flask_mongoengine import MongoEngine

db = MongoEngine()

class Node(db.Document):
    title = db.StringField(required=True)

    def __str__(self):
        return self.title

class User(db.Document):
    pass

class Question(db.Document):
    node = db.ReferenceField(Node)
    text = db.StringField()
    correct_answer = db.StringField()
    distractors = db.ListField(db.StringField())
    solution_explained = db.StringField()

class ReactQuestion(db.Document):
    node = db.ReferenceField(Node)
    component = db.StringField()
    text_intro = db.StringField()
    content = db.ListField(db.DictField())
