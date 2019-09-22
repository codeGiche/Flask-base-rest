from private.apps.auth import AuthApp
from flask_jwt_extended import create_access_token

@AuthApp.authorization
def auth(username, password):
    print(username, password)
    return {'access_token':create_access_token(identity=username)}