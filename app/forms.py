from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    # Определяем форму с полями и берем за основу
    date = DateField('Дата', validators=[DataRequired()])
    sent = IntegerField('Отправлено', validators=[DataRequired()])
    mistakes = IntegerField('Ошибки', validators=[DataRequired()])

class PCRform(MyForm):
    # Форма для ПЦР
    done = IntegerField('Выполнено', validators=[DataRequired()])

class MCEform(MyForm):
    # Форма для МСЭ
    assigned  = IntegerField('Назначено', validators=[DataRequired()])

class SearchForm(FlaskForm):
    # Форма для поиска
    date = DateField('Выбрать даты', validators=[DataRequired()])