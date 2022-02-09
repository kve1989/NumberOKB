from flask import render_template, request, redirect, flash, session, url_for
from app import app, db
from app.models import *
from app.forms import PCRform, SearchForm, tables
from datetime import datetime, date


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400


@app.errorhandler(500)
def internal_server_template(e):
    return render_template('500.html'), 500


@app.route("/", methods=["GET", "POST"])
def home():
    """ Создаем переменную с изменяемой датой, по умолчанию стоит дата на сегодняшний день """
    filter_date = date.today()

    """ Складываем все цифры и название таблицы """
    all_data = []

    form = SearchForm()

    if form.date.data:
        """ Сохраняем дату выбранную пользователем в объявленную переменную и дополнительно в сессию """
        filter_date = form.date.data
        session['date'] = form.date.data

    for table in tables:
        """ Перебираем список с таблицами для выборки цифр """
        all_data += [
            {
                'name': table[1],
                'data': eval(table[0]).query.filter(eval(table[0]).date == filter_date).all()
            }
        ]

    return render_template('index.html', form=form, date=filter_date, all_data=all_data)


@app.route("/pcr", methods=["POST", "GET"])
def page_pcr_index():

    form = SearchForm()

    records = None

    if form.table.data:
        """ В сессию складываем имя таблицы, которую пользователь выбрал на странице"""
        session['table'] = form.table.data
        records = eval(form.table.data).query.order_by(eval(form.table.data).date).all()
    elif form.table.data is None:
        records = eval(session['table']).query.order_by(eval(session['table']).date).all()

    return render_template('pcr/index.html', records=records, form=form, tables=tables)


@app.route("/pcr/create")
def page_pcr_create():
    form = PCRform()
    return render_template('pcr/create.html', form=form, tables=tables)


@app.route("/pcr/<int:id>/edit")
def pcr_page_edit(id):
    form = PCRform()
    record = eval(session['table']).query.get_or_404(id)
    return render_template('pcr/edit.html', form=form, record=record, tables=tables)


@app.route("/pcr/new", methods=['POST'])
def pcr_new():
    date = datetime.strptime(request.form['date'], "%Y-%m-%d")
    done = request.form['done']
    sent = request.form['sent']
    mistakes = request.form['mistakes']

    form = PCRform()

    if form.validate_on_submit():
        record = eval(form.table.data)(date=date, done=done, sent=sent, mistakes=mistakes)
        try:
            db.session.add(record)
            db.session.commit()
            flash("Запись успешно добавлена!", 'success')
        except:
            flash("Ошибка при добавлении!", 'danger')

        return redirect(url_for('page_pcr_index'))

    return render_template('pcr/create.html', form=form)


@app.route("/pcr/<int:id>/update", methods=['POST'])
def pcr_update(id):
    record = eval(session['table']).query.get_or_404(id)
    record.date = datetime.strptime(request.form['date'], "%Y-%m-%d")
    record.done = request.form['done']
    record.sent = request.form['sent']
    record.mistakes = request.form['mistakes']

    form = PCRform()

    if form.validate_on_submit():
        try:
            db.session.commit()
            flash("Запись успешно изменена!", 'success')
        except:
            flash("Ошибка при изменении!", 'danger')

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
