from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

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
    # Определяем форму с полями и берем за основу
    date = DateField('Дата', validators=[DataRequired()])
    sent = IntegerField('Отправлено')
    mistakes = IntegerField('Ошибки')
    done = IntegerField('Выполнено')
    table = SelectField('Таблица', choices=tables, validators=[DataRequired()])


class SearchForm(FlaskForm):
    # Форма для поиска
    table = SelectField('Таблица', choices=tables, validators=[DataRequired()])
    date = DateField('Начало', validators=[DataRequired()])
    date_end = DateField('Конец')


class SignForm(FlaskForm):
    # Форма для создания записи ЭЦП
    # owner = StringField('Владелец ключа', validators=[DataRequired()])
    typeCertificate = SelectField('Тип сертификата', choices=typesCert, validators=[DataRequired()])
    # dateStart = DateField('Дата начала действия', validators=[DataRequired()])
    # dateEnd = DateField('Дата окончания действия', validators=[DataRequired()])
    fileCertificate = FileField('Файл сертификата (.cer)', validators=[
        FileRequired(),
        FileAllowed(['cer'], 'Разрешается только .cer')
    ])
    fileContainer = FileField('Файл контейнера (.pfx/.reg)', validators=[
        FileRequired(),
        FileAllowed(['pfx', 'reg'], 'Разрешается только .pfx или .reg')
    ])