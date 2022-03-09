from email.policy import default
import errno
from flask import render_template, request, redirect, flash, session, url_for
from app import app, db
from app.models import *
from app.forms import Form, SearchForm, tables
from datetime import datetime, date, timedelta

default_date = date.today() - timedelta(days=1)


@app.route("/", methods=["GET", "POST"])
def home():

    """ Создаем форму поиска """
    form = SearchForm()

    """ Создаем переменную с изменяемой датой, по умолчанию стоит дата за вчерашний день """
    filter_date = default_date
    form.date.data = default_date
    form.date_end.data = default_date

    """ Складываем конечную дату """
    end_date = ''

    """ Складываем все цифры и название таблицы """
    all_data = []

    if form.date.data:
        """ Сохраняем дату выбранную пользователем в объявленную переменную и дополнительно в сессию """
        filter_date = form.date.data
        session['date'] = form.date.data

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


@app.route("/pcr", methods=["POST", "GET"], defaults={"page": 1})
@app.route("/pcr/<int:page>", methods=["POST", "GET"])
def page_pcr_index(page):
    # Количество записей на странице
    per_page = 5

    page = page
    """ Форма поиска """
    form = SearchForm()

    records = None

    """ Таблица выбранная пользователем """
    selected_table = None

    if form.table.data:
        """ В сессию и переменную складываем имя таблицы, которую пользователь выбрал на странице"""
        selected_table = form.table.data
        session['table'] = form.table.data

    elif form.table.data is None:
        """ Если таблица не выбрана по умолчанию выставим первую таблицу в списке """
        session['table'] = tables[0][0]
        selected_table = tables[0][0]

    # records = eval(selected_table).query.order_by(eval(selected_table).date).all()
    records = eval(selected_table).query.order_by(eval(selected_table).date).paginate(page, per_page, error_out=False)

    return render_template('pcr/index.html', records=records, form=form, tables=tables)


@app.route("/pcr/create")
def page_pcr_create():
    form = Form()
    return render_template('pcr/create.html', form=form, tables=tables, date=default_date)


@app.route("/pcr/<int:id>/edit")
def pcr_page_edit(id):
    form = Form()
    record = eval(session['table']).query.get_or_404(id)
    return render_template('pcr/edit.html', form=form, record=record, tables=tables)


@app.route("/pcr/new", methods=['POST'])
def pcr_new():
    date = datetime.strptime(request.form['date'], "%Y-%m-%d")

    form = Form()

    if form.is_submitted():
        record = eval(form.table.data)(date=date, done=form.done.data,
                                       sent=form.sent.data, mistakes=form.mistakes.data)

        try:
            db.session.add(record)
            db.session.commit()
            flash("Запись успешно добавлена!", 'success')
        except:
            flash("Ошибка при добавлении!", 'danger')
        return redirect(url_for('page_pcr_index'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

    return render_template('pcr/create.html', form=form)


@app.route("/pcr/<int:id>/update", methods=['POST'])
def pcr_update(id):
    record = eval(session['table']).query.get_or_404(id)
    record.date = datetime.strptime(request.form['date'], "%Y-%m-%d")
    record.done = request.form['done']
    record.sent = request.form['sent']
    record.mistakes = request.form['mistakes']

    form = Form()

    if form.is_submitted():
        try:
            db.session.commit()
            flash("Запись успешно изменена!", 'success')
        except:
            flash("Ошибка при изменении!", 'danger')

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

    return redirect(url_for('page_pcr_index'))


@app.route("/pcr/<int:id>/delete")
def pcr_delete(id):
    record = eval(session['table']).query.get_or_404(id)

    try:
        db.session.delete(record)
        db.session.commit()
        flash("Запись успешно удалена!", 'success')
    except:
        flash("Ошибка при удалении!", 'danger')

    return redirect(url_for('page_pcr_index'))
