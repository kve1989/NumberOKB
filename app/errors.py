from flask import render_template, Blueprint
from werkzeug.exceptions import (NotFound, InternalServerError)

err = Blueprint('err', __name__)

@err.errorhandler(NotFound)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@err.errorhandler(InternalServerError)
def internal_server_template(e):
    return render_template('errors/500.html'), 500
