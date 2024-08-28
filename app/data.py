from flask import render_template, request, redirect, flash, session, url_for, Blueprint
from app import db
from app.models import *
from app.forms import Form, tables
from app.site.forms import SearchForm
from datetime import datetime, date, timedelta

def get_date():
    return date.today() - timedelta(days=1)

default_date = get_date()


data = Blueprint('data', __name__)

@data.route("/data", methods=["POST", "GET"])
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
        """ В сессию и переменную складываем имя таблицы,
        которую пользователь выбрал на странице"""
        selected_table = form.table.data
        session['table'] = form.table.data

    records = eval(selected_table).query.order_by(eval(selected_table).id.desc()).all()

    return render_template('data/index.html', records=records, form=form, tables=tables)


@data.route("/data/create")
def page_data_create():
    form = Form()
    return render_template('data/create.html', form=form, tables=tables, date=get_date())


@data.route("/data/<int:id>/edit")
def page_data_edit(id):
    form = Form()
    record = eval(session['table']).query.get_or_404(id)
    return render_template('data/edit.html', form=form, record=record, tables=tables)


@data.route("/data/new", methods=['POST'])
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
        return redirect(url_for('data.page_data_index'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

    return render_template('data/create.html', form=form)

@data.route("/data/<int:id>/update", methods=['POST'])
def data_update(id):
    record = eval(session['table']).query.get_or_404(id)
    form = Form()
    if request.method == 'POST':
        field_date = datetime.strptime(request.form.get('date'), "%Y-%m-%d")
        field_done = request.form.get('done')
        field_sent = request.form.get('sent')
        field_mistakes = request.form.get('mistakes')

        if field_done != '' and field_sent != '' and field_mistakes != '':
            record.date = field_date
            record.done = field_done
            record.sent = field_sent
            record.mistakes = field_mistakes
            db.session.commit()
            flash("Запись успешно изменена!", 'success')
            return redirect(url_for('page_data_index'))
        else:
            flash("Ошибка при изменении!", 'danger')
            return render_template('data/edit.html', form=form, record=record, tables=tables)

@data.route("/data/<int:id>/delete")
def data_delete(id):
    record = eval(session['table']).query.get_or_404(id)

    try:
        db.session.delete(record)
        db.session.commit()
        flash("Запись успешно удалена!", 'success')
    except:
        flash("Ошибка при удалении!", 'danger')

    return redirect(url_for('page_data_index'))
