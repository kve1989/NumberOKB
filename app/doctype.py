from flask import render_template, request, redirect, flash, url_for, send_from_directory, abort
from . import app, db, admin_page
from .models import DocType
from .forms import DocTypeForm

app.register_blueprint(admin_page, url_prefix='/administration')

@app.route('/doctype')
def page_table_index():
    records = DocType.query.all()
    form = DocTypeForm()
    return render_template('doctype/index.html', records=records, form=form)

@app.route('/doctype/create')
def page_table_create():
    form = DocTypeForm()
    return render_template('doctype/create.html', form=form)


@app.route('/doctype/edit/<int:id>')
def page_table_edit(id):
    form = DocTypeForm()
    record = DocType.query.get_or_404(id)
    return render_template('doctype/edit.html', form=form, record=record)

@app.route('/doctype/store', methods=['POST'])
def table_store():
    form = DocTypeForm()

    if form.validate_on_submit():
        record = DocType(
            name = form.doctype.data.strip(),
        )
        db.session.add(record)
        db.session.commit()
        flash("Запись успешно добавлена!", 'success')
        return redirect(url_for('page_table_index'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

    return render_template('doctype/create.html', form=form)

@app.route('/doctype/<int:id>/update', methods=['POST'])
def table_update(id):
    record = DocType.query.get_or_404(id)
    form = DocTypeForm()

    if request.method == 'POST':
        if record:
            record.name = form.doctype.data.strip()
            db.session.add(record)
            db.session.commit()
            flash("Запись успешно обновлена!", 'success')
            return redirect(url_for('page_table_index'))
    abort(404)

@app.route('/doctype/<int:id>/delete')
def table_delete(id):
    record = DocType.query.get_or_404(id)
    if record:
        db.session.delete(record)
        db.session.commit()
        flash("Запись успешно удалена!", 'success')
        return redirect(url_for('page_table_index'))
    abort(404)