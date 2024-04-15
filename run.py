from app import app, db
from app.models import DocType
import os

doctype = ["Контрольная карта диспансеризации",
"Лабораторные исследования",
"Лабораторные исследования (ПЦР)",
"Медицинские свидетельства о рождении",
"Направление на МСЭ",
"Направление на госпитализацию, восстановительное лечение, обследование, консультацию",
"Протокол инструментальных исследований",
"Молочная смесь",
"Рецепты",
"Экстренное извещение",
"Эпикриз взятия на Д учет",
"Эпикриз снятия с Д учета",
"Вакцинация (Covid)",
"Вызов врача на дом",
"Сведения о смерти",
"Сведения о перинатальной смерти",
"ЭЛН открытых",
"ЭЛН закрытых"]

with app.app_context():
    records = DocType.query.all()
    if len(records) != 0:
        records = DocType.query.delete()
        db.session.commit()
    for item in doctype:
        query = DocType(name=item)
        db.session.add(query)
    db.session.commit()

"""Проверяем на наличие папки для загрузок"""
if (not(os.path.exists(app.config['UPLOAD_FOLDER']))):
    os.mkdir(app.config['UPLOAD_FOLDER'])

if __name__ == '__main__':
    app.run(debug=True)
