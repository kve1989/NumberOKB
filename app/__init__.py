from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

from config import Config

db = SQLAlchemy()
moment = Moment()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()

    db.init_app(app)
    moment.init_app(app)

    with app.app_context():
        db.create_all()

    from app.sign.views import sign
    app.register_blueprint(sign)

    from app.doctype.views import doctype
    app.register_blueprint(doctype)

    from app.dataondocs import dataondocs
    app.register_blueprint(dataondocs)

    from app.data import data
    app.register_blueprint(data)

    from app.site.views import site
    app.register_blueprint(site)

    from app.errors import err
    app.register_blueprint(err)

    return app

# from . import views, errors, models
# from . import data
