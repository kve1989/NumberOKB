from flask import render_template, request, redirect, flash, url_for, send_from_directory, abort, Blueprint
from werkzeug.utils import secure_filename
import os
from . import app, db
from .models import Signs
from .forms import SignForm
from .helpers import generateFilename, parseCertificate

sign = Blueprint('sign', __name__, url_prefix='/sign')

@sign.route('/')
def index():
    records = Signs.query.all()
    form = SignForm()
    return render_template('sign/index.html', page_title='ЭЦП', records=records, form=form)

@sign.route('/store', methods=['POST'])
def store():
    form = SignForm()

    typeCertificate = request.form['typeCertificate']
    fileCertificate = secure_filename( generateFilename(form.fileCertificate.data.filename) )
    fileContainer = secure_filename( generateFilename(form.fileContainer.data.filename) )

    if form.validate_on_submit():
        """Сохраняем контейнер и сертификат в файлы на диск"""
        request.files['fileCertificate'].save(os.path.join(app.config['UPLOAD_FOLDER'], fileCertificate))
        request.files['fileContainer'].save(os.path.join(app.config['UPLOAD_FOLDER'], fileContainer))

        """Здесь храним распарсенный сертификат"""
        parsedCert = parseCertificate(os.path.join(app.config['UPLOAD_FOLDER'], fileCertificate))

        """Проверка на существование имеющегося сертификата в БД по серийному номеру"""
        duplicate_cert = Signs.query.filter_by(serial_number=parsedCert['serial_number']).one_or_none()
        if duplicate_cert:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], fileCertificate))
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], fileContainer))
            flash("Такой сертификат уже есть в хранилице", 'danger')
            return redirect(url_for('sign.index'))

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
        return redirect(url_for('sign.index'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

@sign.route('/<int:id>/delete')
def delete(id):
    record = Signs.query.get_or_404(id)
    if record:
        db.session.delete(record)
        db.session.commit()
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], record.fileCertificate)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], record.fileCertificate))

        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], record.fileContainer)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], record.fileContainer))

        flash("Запись успешно удалена!", 'success')
        return redirect(url_for('sign.index'))
    abort(404)

@app.route('/uploads/<file>')
def download_file(file):
    return send_from_directory(app.config["UPLOAD_FOLDER"], file)
