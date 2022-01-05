from flask import Flask
from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
migrate = Migrate(app,db)
cli = FlaskGroup(app)
from app.models import tables
from app.controllers import routes