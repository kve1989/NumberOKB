from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
moment = Moment(app)
migrate = Migrate(app, db)

from . import views, errors, models
from . import data, sign, doctype