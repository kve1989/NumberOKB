from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import (datetime, date)
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PCR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
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

@app.route("/")
def home():
    records = PCR.query.order_by(PCR.date).all()
    return render_template('index.html', records=records)

@app.route("/create")
def create():
    return render_template('create.html')

@app.route("/new", methods=['POST'])
def new_record():
    date = datetime.strptime(request.form['date'], "%Y-%m-%d")
    done = request.form['done']
    sent = request.form['sent']
    mistakes = request.form['mistakes']

    record = PCR(date=date, done=done,sent=sent,mistakes=mistakes)

    try:
        db.session.add(record)
        db.session.commit()
        return redirect('/')
    except:
        return "Ошибка при добавлении"





if __name__ == '__main__':
    app.run(debug=True)
