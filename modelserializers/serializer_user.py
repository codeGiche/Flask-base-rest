from models.user import ModelUser
from private.serializers.serializer import ModelSchema


class SerializerUser(ModelSchema):
    class Meta:
        model=ModelUser
