from app import db

class DocType(db.Model):
    __tablename__ = 'DocType'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return '<DocType %r>' % self.id
