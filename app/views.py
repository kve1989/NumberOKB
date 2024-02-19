from flask import render_template, session
from datetime import date, timedelta
from . import app, db
from .models import *
from .forms import SearchForm, tables

def get_date():
    return date.today() - timedelta(days=1)

default_date = get_date()

@app.route("/", methods=["GET", "POST"])
def home():

    """ Создаем форму поиска """
    form = SearchForm()

    """ Создаем переменную с изменяемой датой, по умолчанию стоит дата за вчерашний день """
    filter_date = default_date

    """ Складываем конечную дату """
    end_date = None

    """ Складываем все цифры и название таблицы """
    all_data = []

    if form.is_submitted():
        """ Сохраняем дату выбранную пользователем в объявленную переменную и дополнительно в сессию """
        filter_date = form.date.data
        session['date'] = form.date.data
        end_date = form.date_end.data

    for table in tables:
        """ Перебираем список с таблицами для выборки цифр """
        end_date = form.date_end.data

        querySelectAllDataFromAllTables = eval(table[0]).query.filter(eval(table[0]).date == filter_date).all()

        if form.date_end.data is not None:
            querySelectAllDataFromAllTables = eval(table[0]).query.filter(eval(table[0]).date.between(filter_date, end_date)).all()

        all_data += [
            {
                'name': table[1],
                'data': querySelectAllDataFromAllTables
            }
        ]

    return render_template('index.html', form=form, date=filter_date, end_date=end_date, all_data=all_data)
