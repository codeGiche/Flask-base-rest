from modelserializers.serializer_user import SerializerUser, ModelUser
from ..api_swagger.swagger_user_protect import ns_user_protect, get_response, user_post_query
from .. import Resource

from flask_jwt_extended import jwt_required

@ns_user_protect.route('')
class RestUser(Resource):
    decorators = [jwt_required]

    _serializer = SerializerUser()
    _serializer_many = SerializerUser(many=True)

    @ns_user_protect.marshal_with(get_response)
    @ns_user_protect.expect(user_post_query)
    def get(self):
        user = ModelUser.query.all()
        serUser = self._serializer_many.dump(user)

        return {
            'users':serUser
        }