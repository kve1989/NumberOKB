from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    date = DateField('Дата', validators=[DataRequired()])
    sent = IntegerField('Отправлено', validators=[DataRequired()])
    mistakes = IntegerField('Ошибки', validators=[DataRequired()])

class PCRform(MyForm):
    done = IntegerField('Выполнено', validators=[DataRequired()])

class MCEform(MyForm):
    assigned  = IntegerField('Назначено', validators=[DataRequired()])

class SearchForm(FlaskForm):
    date = DateField('Выбрать даты', validators=[DataRequired()])