from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class DocTypeForm(FlaskForm):
    doctype = StringField('Название таблицы', validators=[DataRequired()])
