from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from dynaconf import FlaskDynaconf

db = SQLAlchemy()
migrate = Migrate()
api = Api()
dynaconf = FlaskDynaconf()
