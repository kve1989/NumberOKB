from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_migrate import Migrate
from config import Config
from .admin import admin as admin_blueprint

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(admin_blueprint)

db = SQLAlchemy(app)
moment = Moment(app)
migrate = Migrate(app, db)

from app import views, errors, models, admin
