import bcrypt
from mrmccue.models.user import User

def register_user(username, password):
    if User.objects(username=username):
        return
    password = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    new_user = User(username, hashed)
    new_user.save()
