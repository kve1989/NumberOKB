from flask import render_template, request, redirect, flash, session, url_for, send_from_directory, abort
from app import app, db
from app.models import Tables
from app.forms import TablesForm

@app.route('/table')
def page_table_index():
    records = Tables.query.all()
    return render_template('table/index.html', records=records)

@app.route('/table/create')
def page_table_create():
    form = TablesForm()
    return render_template('table/create.html', form=form)


@app.route('/table/edit/<int:id>')
def page_table_edit(id):
    form = TablesForm()
    record = Tables.query.get_or_404(id)
    return render_template('table/edit.html', form=form, record=record)

@app.route('/table/store', methods=['POST'])
def table_store():
    form = TablesForm()

    if form.validate_on_submit():
        record = Tables(
            name = form.table.data.strip(),
        )
        db.session.add(record)
        db.session.commit()
        flash("Запись успешно добавлена!", 'success')
        return redirect(url_for('page_table_index'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')

    return render_template('table/create.html', form=form)

@app.route('/table/<int:id>/update', methods=['POST'])
def table_update(id):
    record = Tables.query.get_or_404(id)
    form = TablesForm()

    if request.method == 'POST':
        if record:
            record.name = form.table.data.strip()
            db.session.add(record)
            db.session.commit()
            flash("Запись успешно обновлена!", 'success')
            return redirect(url_for('page_table_index'))
    abort(404)

@app.route('/table/<int:id>/delete')
def table_delete(id):
    record = Tables.query.get_or_404(id)
    if record:
        db.session.delete(record)
        db.session.commit()
        flash("Запись успешно удалена!", 'success')
        return redirect(url_for('page_table_index'))
    abort(404)