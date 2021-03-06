from databases.dbs import db


class ModelUser(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    email = db.Column(db.String(200),nullable=False,unique=True)