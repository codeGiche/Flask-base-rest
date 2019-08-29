from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
serializerApp = Marshmallow()
restApi = Api(prefix='/api/v1')