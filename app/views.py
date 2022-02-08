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
    filter_date = date.today()

    form = SearchForm()

    if form.date.data:
        filter_date = form.date.data
        session['date'] = form.date.data

    pcr_all = PCR.query.filter(PCR.date == filter_date).all()
    return render_template('index.html', pcr_all=pcr_all, form=form, date=filter_date)


@app.route("/pcr", methods=["POST", "GET"])
def page_pcr_index():
    form = SearchForm()

    # records = PCR.query.order_by(PCR.date).all()
    records = None

    if form.table.data:
        session['table'] = form.table.data
        records = eval(form.table.data).query.order_by(eval(form.table.data).date).all()

    return render_template('pcr/index.html', records=records, form=form, title="ПЦР")


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
        # record = PCR(date=date, done=done, sent=sent, mistakes=mistakes)
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
    form = PCRform()

    record = eval(session['table']).query.get_or_404(id)
    record.date = datetime.strptime(request.form['date'], "%Y-%m-%d")
    record.done = request.form['done']
    record.sent = request.form['sent']
    record.mistakes = request.form['mistakes']

    if form.validate_on_submit():
        try:
            if form.table.data != session['table']:
                db.session.remove(record)
                db.session.commit()
                record = eval(form.table.date)(date=datetime.strptime(form.date.data, "%Y-%m-%d"),
                                               done=form.done.data,
                                               sent=form.sent.data,
                                               mistakes=form.mistakes.data)
                db.session.add(record)
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
