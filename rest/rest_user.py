from flask import request
from flask_restful import Resource

from exts import restApi
from exts import db

from serializers.modelSerializers import SerializerUser,User

class RestUser(Resource):
    _serializer = SerializerUser()

    def get(self,id=None):
        if id:
            user = User.query.get(id)
            serUser = SerializerUser()
        else:
            user = User.query.all()
            serUser = SerializerUser(many=True)
        return serUser.dump(user)

    def post(self):
        json = request.get_json()

        user = self._serializer.load(json)
        db.session.add(user)
        db.session.commit()

        return self._serializer.dump(user)

class RestUserById(RestUser):
    def put(self,id):
        json = request.get_json()
        user = User.query.get(id)

        for attr in json:
            if hasattr(user,attr):
                setattr(user,attr,json[attr])
        print(user.name)
        db.session.add(user)
        db.session.commit()
        return self._serializer.dump(user)

restApi.add_resource(RestUser,'/user')
restApi.add_resource(RestUserById,'/user/<int:id>')




