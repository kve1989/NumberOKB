from flask import render_template, request, redirect, flash, url_for, abort, Blueprint
from app import db
from .models import DocType
from .forms import DocTypeForm

doctype = Blueprint('doctype', __name__, url_prefix='/doctype')

@doctype.route('/')
def index():
    records = DocType.query.all()
    form = DocTypeForm()
    return render_template('doctype/index.html', page_title='Типы документов', records=records, form=form)

@doctype.route('/create')
def create():
    form = DocTypeForm()
    return render_template('doctype/create.html', form=form)

@doctype.route('/edit/<int:id>')
def edit(id):
    form = DocTypeForm()
    record = DocType.query.get_or_404(id)
    return render_template('doctype/edit.html', form=form, record=record)

@doctype.route('/store', methods=['POST'])
def store():
    form = DocTypeForm()

    if form.validate_on_submit():
        record = DocType(
            name = form.doctype.data.strip(),
        )
        db.session.add(record)
        db.session.commit()
        flash("Запись успешно добавлена!", 'success')
        return redirect(url_for('doctype.index'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

    return render_template('doctype/create.html', form=form)

@doctype.route('/<int:id>/update', methods=['POST'])
def update(id):
    record = DocType.query.get_or_404(id)
    form = DocTypeForm()

    if request.method == 'POST':
        if record:
            record.name = form.doctype.data.strip()
            db.session.add(record)
            db.session.commit()
            flash("Запись успешно обновлена!", 'success')
            return redirect(url_for('doctype.index'))
    abort(404)

@doctype.route('/<int:id>/delete')
def delete(id):
    record = DocType.query.get_or_404(id)
    if record:
        db.session.delete(record)
        db.session.commit()
        flash("Запись успешно удалена!", 'success')
        return redirect(url_for('doctype.index'))
    abort(404)
