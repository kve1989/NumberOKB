from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

tables = [
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
    ('VaccinationAll', '20. Вакцинация (вся)'),
    ('VaccinationCovid', '21. Вакцинация (Covid)'),
    ('CallDocAtHome', '22. Вызов врача на дом'),
    ('DeathInform', '23. Сведения о смерти'),
    ('InformPerinatalDeath', '24. Сведения о перинатальной смерти'),
    ('ELNOpen', '25. ЭЛН открытых'),
    ('ELNClose', '26. ЭЛН закрытых')
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
    date = DateField('Выбрать даты', validators=[DataRequired()])
