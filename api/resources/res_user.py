from flask import request
from marshmallow.exceptions import ValidationError

from ..api_swagger.swagger_user import (ns_user, get_response, user_model, \
                                          user_post_query, )
from databases.dbs import db
from modelserializers.serializer_user import SerializerUser, ModelUser
from .. import Resource, abort


@ns_user.route('')
class RestUser(Resource):
    _serializer = SerializerUser()
    _serializer_many = SerializerUser(many=True)

    @ns_user.marshal_with(get_response)
    def get(self):
        user = ModelUser.query.all()
        serUser = self._serializer_many.dump(user)

        return {
            'users':serUser
        }

    @ns_user.expect(user_post_query)
    @ns_user.marshal_with(user_model)
    def post(self):
        json = request.get_json() or request.args.to_dict()
        if not json:
            return abort(400,error='Invalid request')

        print(json)

        try:
            user = self._serializer.load(json)
        except ValidationError as e:
            abort(400,error=e.messages)

        db.session.add(user)
        db.session.commit()
        db.session.flush()

        return self._serializer.dump(user), 200

@ns_user.route('/<int:id>')
class RestUserById(Resource):

    @ns_user.marshal_with(user_model)
    def get(self,id):
        user = ModelUser.query.get(id)
        return self._serializer.dump(user)

    def put(self,id):
        json = request.get_json()
        user = ModelUser.query.get(id)

        for attr in json:
            if hasattr(user,attr):
                setattr(user,attr,json[attr])

        db.session.add(user)
        db.session.commit()
        return self._serializer.dump(user)