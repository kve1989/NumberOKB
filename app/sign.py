from flask import render_template, request, redirect, flash, url_for, send_from_directory, abort
from werkzeug.utils import secure_filename
import os
from . import app, db
from .models import Signs
from .forms import SignForm
from .helpers import generateFilename, parseCertificate

@app.route('/sign')
def page_sign_index():
    records = Signs.query.all()
    form = SignForm()
    return render_template('sign/index.html', records=records, form=form)

@app.route('/sign/store', methods=['POST'])
def sign_store():
    form = SignForm()

    typeCertificate = request.form['typeCertificate']
    fileCertificate = secure_filename( generateFilename(form.fileCertificate.data.filename) )
    fileContainer = secure_filename( generateFilename(form.fileContainer.data.filename) )

    if form.validate_on_submit():
        request.files['fileCertificate'].save(os.path.join(app.config['UPLOAD_FOLDER'], fileCertificate))
        request.files['fileContainer'].save(os.path.join(app.config['UPLOAD_FOLDER'], fileContainer))

        parsedCert = parseCertificate(os.path.join(app.config['UPLOAD_FOLDER'], fileCertificate))

        record = Signs(
            owner = parsedCert['surname'] + ' ' + parsedCert['givenName'],
            type = typeCertificate,
            dateStart = parsedCert['dateStart'],
            dateEnd = parsedCert['dateEnd'],
            fileCertificate = fileCertificate,
            fileContainer = fileContainer,
            issuer = parsedCert['issuer'],
            serial_number = parsedCert['serial_number']
        )
        db.session.add(record)
        db.session.commit()
        flash("Запись успешно добавлена!", 'success')
        return redirect(url_for('page_sign_index'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

    return render_template('sign/create.html', form=form)

@app.route('/sign/<int:id>/delete')
def sign_delete(id):
    record = Signs.query.get_or_404(id)
    if record:
        db.session.delete(record)
        db.session.commit()
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], record.fileCertificate)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], record.fileCertificate))

        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], record.fileContainer)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], record.fileContainer))

        flash("Запись успешно удалена!", 'success')
        return redirect(url_for('page_sign_index'))
    abort(404)

@app.route('/uploads/<file>')
def download_file(file):
    return send_from_directory(app.config["UPLOAD_FOLDER"], file)