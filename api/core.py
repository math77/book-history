from flask import Flask
from config import Config
from extensions import db, migrate, api, dynaconf
from api.resources.client import ClientResource
from api import models


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    dynaconf.init_app(app)

    api.add_resource(ClientResource, '/client', '/client/<int:id_client>')
    #api.add_resource(ClientResource, '/client/<int: id_client>')
    return app
