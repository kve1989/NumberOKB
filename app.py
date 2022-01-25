from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

from forms import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '01f260718007c0bd2ef3e9005b84ab97'

db = SQLAlchemy(app)

class PCR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=False)
    sent = db.Column(db.Integer, nullable=False)
    mistakes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<PCR %r>' % self.id

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400

@app.errorhandler(500)
def internal_server_template(e):
    return render_template('500.html'), 500

@app.route("/create", methods=['GET', 'POST'])
def create():
    form = PCRform()
    return render_template('create.html', form=form)

@app.route("/")
def home():
    records = PCR.query.order_by(PCR.date).all()
    return render_template('index.html', records=records)

@app.route("/new", methods=['POST'])
def new_record():
    date = datetime.strptime(request.form['date'], "%Y-%m-%d")
    done = request.form['done']
    sent = request.form['sent']
    mistakes = request.form['mistakes']

    form=PCRform()

    if form.validate_on_submit():
        record = PCR(date=date, done=done,sent=sent,mistakes=mistakes)
        try:
            db.session.add(record)
            db.session.commit()
            flash("Запись успешно добавлена!", 'success')
            return redirect('/')
        except:
            return "Ошибка при добавлении"

    return render_template('create.html', form=form)

@app.route("/<int:id>/delete")
def delete_record(id):
    record = PCR.query.get_or_404(id)

    try:
        db.session.delete(record)
        db.session.commit()
        flash("Запись успешно удалена!", 'success')
        return redirect('/')
    except:
        flash("Запись успешно удалена!", 'error')
        return redirect('/')

@app.route("/<int:id>/edit")
def edit_record(id):
    form = PCRform()
    record = PCR.query.get_or_404(id)
    return render_template('edit.html', form=form, record=record)

@app.route("/<int:id>/update", methods=['POST'])
def update_record(id):
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
            return redirect('/')
        except:
            return "Ошибка при изменении"

    return render_template('edit.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
