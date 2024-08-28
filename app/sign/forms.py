from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SelectField
from wtforms.validators import DataRequired
from app import db
import sqlalchemy as sa

typesCert = [
    ('individual', 'Физическое лицо'),
    ('personal', 'Должностное лицо'),
    ('organdname', 'Юридическое лицо'),
    ('organization', 'Юридическое лицо без ФИО')
]

class SignForm(FlaskForm):
    """Форма для добавления ЭЦП"""
    typeCertificate = SelectField('Тип сертификата', choices=typesCert, validators=[DataRequired()])
    fileCertificate = FileField('Файл сертификата (.cer)', validators=[
        FileRequired(),
        FileAllowed(['cer'], 'Разрешается только .cer')
    ])
    fileContainer = FileField('Файл контейнера (.pfx/.reg)', validators=[
        FileRequired(),
        FileAllowed(['pfx', 'reg'], 'Разрешается только .pfx или .reg')
    ])
