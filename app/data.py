from flask import render_template, request, redirect, flash, session, url_for
from app import app, db
from app.models import *
from app.forms import Form, SearchForm, tables
from app.views import default_date
from datetime import datetime


@app.route("/data", methods=["POST", "GET"])
def page_data_index():
    """ Форма поиска """
    form = SearchForm()

    records = None

    """ Таблица по умолчанию """
    if session.get('table'):
        selected_table = session['table']
    else:
        selected_table = session['table'] = tables[0][0]

    if form.is_submitted():
        """ В сессию и переменную складываем имя таблицы, которую пользователь выбрал на странице"""
        selected_table = form.table.data
        session['table'] = form.table.data

    records = eval(selected_table).query.order_by(eval(selected_table).id.desc()).all()

    return render_template('data/index.html', records=records, form=form, tables=tables)


@app.route("/data/create")
def page_data_create():
    form = Form()
    return render_template('data/create.html', form=form, tables=tables, date=default_date)


@app.route("/data/<int:id>/edit")
def page_data_edit(id):
    form = Form()
    record = eval(session['table']).query.get_or_404(id)
    return render_template('data/edit.html', form=form, record=record, tables=tables)


@app.route("/data/new", methods=['POST'])
def data_store():
    date = datetime.strptime(request.form['date'], "%Y-%m-%d")

    form = Form()

    if form.is_submitted():
        record = eval(form.table.data)(date=date,
                                        done=form.done.data,
                                        sent=form.sent.data,
                                        mistakes=form.mistakes.data)

        try:
            db.session.add(record)
            db.session.commit()
            flash("Запись успешно добавлена!", 'success')
        except:
            flash("Ошибка при добавлении!", 'danger')
        return redirect(url_for('page_data_index'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

    return render_template('data/create.html', form=form)


@app.route("/data/<int:id>/update", methods=['POST'])
def data_update(id):
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

    return redirect(url_for('page_data_index'))


@app.route("/data/<int:id>/delete")
def data_delete(id):
    record = eval(session['table']).query.get_or_404(id)

    try:
        db.session.delete(record)
        db.session.commit()
        flash("Запись успешно удалена!", 'success')
    except:
        flash("Ошибка при удалении!", 'danger')

    return redirect(url_for('page_data_index'))