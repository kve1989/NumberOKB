from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.app_context().push()

db = SQLAlchemy(app)
moment = Moment(app)
migrate = Migrate(app, db)

from .sign import sign
app.register_blueprint(sign)
from .doctype import doctype
app.register_blueprint(doctype)
from .dataondocs import dataondocs
app.register_blueprint(dataondocs)

from . import views, errors, models
from . import data
