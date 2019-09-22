from flask_restplus import Api, fields, Resource, abort, abort
from flask_jwt_extended import JWTManager

resApi = Api(prefix='/api/v1')
jwt = JWTManager()