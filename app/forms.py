from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired
from .models import DocType
from . import db
import sqlalchemy as sa

tables = [
    # ('ProtocConsult', 'Протокол консультации'),
    ('ProfMedicalExam', 'Контрольная карта диспансеризации'),
    ('LabResearch',  'Лабораторные исследования'),
    ('LabResPCR', 'Лабораторные исследования (ПЦР)'),
    ('MedCertBirth', 'Медицинские свидетельства о рождении'),
    ('DirectionOnMCE', 'Направление на МСЭ'),
    ('DirectToHospRehabExamCons', 'Направление на госпитализацию, восстановительное лечение, обследование, консультацию'),
    ('ProtocInstrumentStudies',  'Протокол инструментальных исследований'),
    ('MilkMixture', 'Молочная смесь'),
    ('Recipes', 'Рецепты'),
    # ('Statcard', 'Статкарта'),
    ('EmergencyNotice', 'Экстренное извещение'),
    # ('EpicrisisExtrFromPatientsMedRecs', 'Эпикриз Выписка из медицинской документации пациента'),
    ('EpicrisisDaccounting', 'Эпикриз взятия на Д учет'),
    # ('EpicrisisDischarge', 'Эпикриз выписной'),
    # ('EpicrisisTranslation', 'Эпикриз переводной'),
    # ('EpicrisisPosthumous', 'Эпикриз посмертный'),
    # ('EpicrisisPreoperative', 'Эпикриз предоперационный'),
    ('EpicrisisDremoval', 'Эпикриз снятия с Д учета'),
    # ('EpicrisisStage', 'Эпикриз этапный'),
    # ('VaccinationAll', 'Вакцинация (вся)'),
    ('VaccinationCovid', 'Вакцинация (Covid)'),
    ('CallDocAtHome', 'Вызов врача на дом'),
    ('DeathInform', 'Сведения о смерти'),
    ('InformPerinatalDeath', 'Сведения о перинатальной смерти'),
    ('ELNOpen', 'ЭЛН открытых'),
    ('ELNClose', 'ЭЛН закрытых')
]

typesCert = [
    ('individual', 'Физическое лицо'),
    ('personal', 'Должностное лицо'),
    ('organdname', 'Юридическое лицо'),
    ('organization', 'Юридическое лицо без ФИО')
]

class Form(FlaskForm):
    """Определяем форму с полями и берем за основу"""
    date = DateField('Дата', validators=[DataRequired()])
    sent = IntegerField('Отправлено')
    mistakes = IntegerField('Ошибки')
    done = IntegerField('Выполнено')
    table = SelectField('Таблица', choices=tables, validators=[DataRequired()])


class SearchForm(FlaskForm):
    """Форма для поиска"""
    table = SelectField('Таблица', choices=tables, validators=[DataRequired()])
    date = DateField('Начало', validators=[DataRequired()])
    date_end = DateField('Конец')


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

class DocTypeForm(FlaskForm):
    doctype = StringField('Название таблицы', validators=[DataRequired()])

class DataOnDocsForm(FlaskForm):
    query = db.session.scalars(sa.select(DocType)).all()
    doctypes = [['', '']]
    selected_doctype = 0
    for p in query:
        doctypes.append([p.id, p.name])
    # if request.args.get('doctype'):
    #     selected_doctype = request.args.get('doctype')

    date = DateField('Дата', validators=[DataRequired()])
    sent = IntegerField('Отправлено', validators=[DataRequired()])
    mistakes = IntegerField('Ошибки', validators=[DataRequired()])
    done = IntegerField('Выполнено', validators=[DataRequired()])
    doctype = SelectField('Документ', choices=doctypes, default=selected_doctype, validators=[DataRequired()])