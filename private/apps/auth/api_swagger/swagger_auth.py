from private.api.resapi import resApi, Resource, fields

ns_auth = resApi.namespace('auth')

#MODEL

#RESPONSE

post_response = resApi.model('access_token',{
    'access_token': fields.String
})

#QUERY

auth_post_query = ns_auth.parser()
auth_post_query.add_argument('Authorization', type=str, required=True, location='headers')
