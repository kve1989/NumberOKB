from flask_sqlalchemy import SQLAlchemy
from app import db

class PCR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=False)
    sent = db.Column(db.Integer, nullable=False)
    mistakes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<PCR %r>' % self.id