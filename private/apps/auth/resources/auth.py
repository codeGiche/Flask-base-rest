from flask_restplus import Resource
from flask import request
from ..api_swagger.swagger_auth import post_response, ns_auth, auth_post_query

@ns_auth.route('')
class AuthResource(Resource):
    _func = None

    @ns_auth.expect(auth_post_query)
    @ns_auth.marshal_with(post_response)
    def post(self):
        username = request.authorization['username']
        password = request.authorization['password']
        return self._func(username, password)
