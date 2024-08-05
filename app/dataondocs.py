from flask import render_template, request, redirect, flash, url_for, abort, Blueprint
from . import db
from .models import DataOnDocs, DocType
from .forms import DataOnDocsForm
from datetime import datetime
import sqlalchemy as sa

dataondocs = Blueprint('dataondocs', __name__, url_prefix='/dataondocs')

@dataondocs.route('/')
def index():
    records = DataOnDocs.query.all()
    if request.args.get('doctype'):
        query = sa.select(DataOnDocs).where(DataOnDocs.doctype_id.like(request.args['doctype']))
        records = db.session.scalars(query).all()
    doctypes = DocType.query.all()
    form = DataOnDocsForm()
    return render_template('/dataondocs/index.html', records=records, doctypes=doctypes, form=form)

@dataondocs.route('/edit/<int:id>')
def edit_record(id):
    record = DataOnDocs.query.all()
    form = DataOnDocsForm()
    pass

@dataondocs.route('/store', methods=['POST'])
def add_record():
    form = DataOnDocsForm()
    if form.validate_on_submit():
        record = DataOnDocs(
            date = datetime.strptime(request.form['date'], "%Y-%m-%d"),
            done = form.done.data,
            sent = form.sent.data,
            mistakes = form.mistakes.data,
            doctype_id = form.doctype.data
        )
        db.session.add(record)
        db.session.commit()
        flash("Запись успешно добавлена!", 'success')
        return redirect(url_for('dataondocs.index'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

@dataondocs.route('/delete/<int:id>')
def delete_record(id):
    record = db.session.get(DataOnDocs, id)
    if record:
        db.session.delete(record)
        db.session.commit()
        flash("Запись успешно удалена!", 'success')
        return redirect(url_for('dataondocs.index'))
    abort(404)
