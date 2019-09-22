from .. import namespace, fields, model

ns_user_protect = namespace('protect/user')

#MODEL
user_model = model('model_user',{
    'name': fields.String,
    'id': fields.Integer,
    'email': fields.String,
    'music': fields.Nested(model('user styles', {
       'styles':fields.List(fields.String)
    }))
})

#RESPONSE
get_response = model('user', {
    'users':fields.List(fields.Nested(user_model))
})

#QUERY
user_post_query = ns_user_protect.parser()
user_post_query.add_argument('access_token', type=str, required=True)