from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

tables = [
    ('', 'Выберете таблицу...'),
    ('ProtocConsult', '1. Протокол консультации'),
    ('ProfMedicalExam', '2. Контрольная карта диспансеризации'),
    ('LabResearch', '3. Лабораторные исследования'),
    ('MedCertBirth', '4. Медицинские свидетельства о рождении'),
    ('DirectionOnMCE', '5. Направление на МСЭ'),
    ('DirectToHospRehabExamCons', '6. Направление на госпитализацию, восстановительное лечение, обследование, консультацию'),
    ('ProtocInstrumentStudies', '7. Протокол инструментальных исследований'),
    ('MilkMixture', '8. Молочная смесь'),
    ('Recipes', '9. Рецепты'),
    ('Statcard', '10. Статкарта'),
    ('EmergencyNotice', '11. Экстренное извещение'),
    ('EpicrisisExtrFromPatientsMedRecs', '12. Эпикриз Выписка из медицинской документации пациента'),
    ('EpicrisisDaccounting', '13. Эпикриз взятия на Д учет'),
    ('EpicrisisDischarge', '14. Эпикриз выписной'),
    ('EpicrisisTranslation', '15. Эпикриз переводной'),
    ('EpicrisisPosthumous', '16. Эпикриз посмертный'),
    ('EpicrisisPreoperative', '17. Эпикриз предоперационный'),
    ('EpicrisisDremoval', '18. Эпикриз снятия с Д учета'),
    ('EpicrisisStage', '19. Эпикриз этапный'),
    ('Vaccination', '20. Вакцинация (вся)'),
    ('CallDocAtHome', '21. Вызов врача на дом'),
    ('DeathInform', '22. Сведения о смерти'),
    ('InformPerinatalDeath', '23. Сведения о перинатальной смерти'),
    ('ELNOpen', '24. ЭЛН открытых'),
    ('ELNClose','25. ЭЛН открытых')
]


class MyForm(FlaskForm):
    # Определяем форму с полями и берем за основу
    date = DateField('Дата', validators=[DataRequired()])
    sent = IntegerField('Отправлено', validators=[DataRequired()])
    mistakes = IntegerField('Ошибки', validators=[DataRequired()])
    table = SelectField('Таблица', choices=tables, validators=[DataRequired()])


class PCRform(MyForm):
    # Форма для ПЦР
    done = IntegerField('Выполнено', validators=[DataRequired()])


class SearchForm(FlaskForm):
    # Форма для поиска
    table = SelectField('Таблица', choices=tables, validators=[DataRequired()])
    date = DateField('Выбрать даты', validators=[DataRequired()])
