from mrmccue import db

class User(db.Document):
    username = db.StringField(max_length=25)
    password_hash = db.StringField(required=True)
