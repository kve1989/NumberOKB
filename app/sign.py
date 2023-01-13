from flask import render_template, request, redirect, flash, session, url_for
from app import app, db
from app.models import Signs
from app.forms import SignForm
from datetime import datetime
from werkzeug.utils import secure_filename

@app.route('/sign')
def page_sign_index():
    records = Signs.query.all()
    return render_template('signs/index.html', records=records)

@app.route('/sign/create')
def page_sign_create():
    form = SignForm()
    return render_template('signs/create.html', form=form)

@app.route('/sign/<int:id>/edit')
def page_sign_edit(id):
    pass

@app.route('/sign/store', methods=['POST'])
def sign_store():
    form = SignForm()

    dateStart = datetime.strptime(request.form['dateStart'], "%Y-%m-%d")
    dateEnd = datetime.strptime(request.form['dateEnd'], "%Y-%m-%d")
    owner = request.form['owner']
    typeCertificate = request.form['typeCertificate']
    fileCertificate = secure_filename(form.fileCertificate.data.filename)
    fileContainer = secure_filename(form.fileContainer.data.filename)

    if form.validate_on_submit():
        record = Signs(
            owner = owner,
            type = typeCertificate,
            dateStart = dateStart,
            dateEnd = dateEnd,
            fileCertificate = fileCertificate,
            fileContainer = fileContainer
        )

        try:
            db.session.add(record)
            db.session.commit()
            flash("Запись успешно добавлена!", 'success')
        except:
            flash("Ошибка при добавлении!", 'danger')
        return redirect(url_for('page_sign_index'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

    return render_template('signs/create.html', form=form)


@app.route('/sign/<int:id>/update')
def sign_update(id):
    pass

@app.route('/sign/<int:id>/delete')
def sign_delete(id):
    record = Signs.query.get_or_404(id)

    try:
        db.session.delete(record)
        db.session.commit()
        flash("Запись успешно удалена!", 'success')
    except:
        flash("Ошибка при удалении!", 'danger')

    return redirect(url_for('page_sign_index'))