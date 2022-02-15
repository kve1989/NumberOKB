from flask import render_template, Blueprint, request, redirect, url_for, Response

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def index():
    return render_template('admin/index.html')


@admin.route('/admin/tables')
def tables():
    from .models import TablesInCurrentBase
    tables = TablesInCurrentBase.query.all()
    return render_template('admin/tables.html', tables=tables)

@admin.route('/admin/tables/<int:id>/changestatus', methods=['GET', 'POST'])
def change_status(id):
    from .models import TablesInCurrentBase
    from app import db
    table = TablesInCurrentBase.query.get_or_404(id)
    table.status = int(request.args['status'])
    db.session.commit()
    return redirect(url_for('admin.tables'))
