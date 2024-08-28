from flask_wtf import FlaskForm
from wtforms import DateField, SelectField
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

class SearchForm(FlaskForm):
    """Форма для поиска"""
    table = SelectField('Таблица', choices=tables, validators=[DataRequired()])
    date = DateField('Начало', validators=[DataRequired()])
    date_end = DateField('Конец')
