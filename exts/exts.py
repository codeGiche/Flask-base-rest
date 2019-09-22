from databases.dbs import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager

cors = CORS(resources={})
jwt = JWTManager()