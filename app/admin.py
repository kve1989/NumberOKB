from flask import render_template

from app import app,db

@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')