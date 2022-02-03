from flask import render_template, request, redirect, flash, session, url_for
from app import app, db
from app.models import PCR
from app.forms import PCRform, SearchForm
from datetime import datetime

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400

@app.errorhandler(500)
def internal_server_template(e):
    return render_template('500.html'), 500

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/pcr", methods=["POST", "GET"])
def pcr_index():
    # today = date.today()
    form = SearchForm()
    records = PCR.query.order_by(PCR.date).all()
    # if request.method == "POST":
    #     session['custom_date'] = request.form['date']
    #     records = PCR.query.order_by(PCR.date).filter(PCR.date >= session['custom_date']).all()
    #     return render_template('index.html', records=records, form=form, today=session['custom_date'])
    return render_template('pcr/index.html', records=records, form=form)

@app.route("/pcr/create")
def page_pcr_create():
    form = PCRform()
    return render_template('pcr/create.html', form=form)

@app.route("/pcr/new", methods=['POST'])
def pcr_new():
    date = datetime.strptime(request.form['date'], "%Y-%m-%d")
    done = request.form['done']
    sent = request.form['sent']
    mistakes = request.form['mistakes']

    form = PCRform()

    if form.validate_on_submit():
        record = PCR(date=date, done=done,sent=sent,mistakes=mistakes)
        try:
            db.session.add(record)
            db.session.commit()
            flash("Запись успешно добавлена!", 'success')
            return redirect(url_for('pcr_index'))
        except:
            return "Ошибка при добавлении"

    return render_template('pcr/create.html', form=form)

@app.route("/pcr/<int:id>/delete")
def pcr_delete(id):
    record = PCR.query.get_or_404(id)

    try:
        db.session.delete(record)
        db.session.commit()
        flash("Запись успешно удалена!", 'success')
    except:
        flash("Ошибка при удалении!", 'danger')

    return redirect(url_for('pcr_index'))

@app.route("/pcr/<int:id>/edit")
def pcr_page_edit(id):
    form = PCRform()
    record = PCR.query.get_or_404(id)
    return render_template('pcr/edit.html', form=form, record=record)

@app.route("/pcr/<int:id>/update", methods=['POST'])
def pcr_update(id):
    record = PCR.query.get_or_404(id)
    record.date = datetime.strptime(request.form['date'], "%Y-%m-%d")
    record.done = request.form['done']
    record.sent = request.form['sent']
    record.mistakes = request.form['mistakes']

    form=PCRform()

    if form.validate_on_submit():
        try:
            db.session.commit()
            flash("Запись успешно изменена!", 'success')
        except:
            flash("Ошибка при изменении!", 'danger')

    return redirect(url_for('pcr_index'))