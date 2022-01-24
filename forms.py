from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    date = DateField('Дата', validators=[DataRequired()])
    sent = StringField('Отправлено', validators=[DataRequired()])
    mistakes = StringField('Ошибки', validators=[DataRequired()])

class PCRform(MyForm):
    done = StringField('Выполнено', validators=[DataRequired()])

class MCEform(MyForm):
    assigned  = StringField('Назначено', validators=[DataRequired()])