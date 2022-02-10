from flask import render_template
from app import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400


@app.errorhandler(500)
def internal_server_template(e):
    return render_template('500.html'), 500