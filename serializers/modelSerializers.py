from .serializer import ModelSchema
from models.user import User


class SerializerUser(ModelSchema):
    class Meta:
        model=User
