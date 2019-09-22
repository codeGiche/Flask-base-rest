class Auth:
    def __init__(self):
        self.dec_auth = None

    def getAuth(self, username, password):
        if self.dec_auth:
            return self.dec_auth(username,password)

    def init_app(self, app):
        if app.config.get('FLASK_APP_AUTH', None) == True:
            from .resources.auth import AuthResource
            AuthResource._func = self.getAuth

    def authorization(self, func):
        self.dec_auth = func


AuthApp = Auth()