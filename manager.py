from flask_migrate import Migrate,Manager,MigrateCommand
from flask import Flask
from database import db
from models.user import *

app = Flask(__name__)
app.config.from_object('config.Developement')

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()