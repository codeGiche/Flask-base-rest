from flask_marshmallow import Marshmallow

serializerApp = Marshmallow()

class ModelSchema(serializerApp.ModelSchema):
    pass

class Schema(serializerApp.Schema):
    pass

class TableSchema(serializerApp.TableSchema):
    pass