from .. import fields, model, namespace

ns_user = namespace('user')

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
user_post_query = ns_user.parser()
user_post_query.add_argument('name', type=str, nullable=False)
user_post_query.add_argument('email', type=str, nullable=False, required=True)