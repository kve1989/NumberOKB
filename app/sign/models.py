from app import db

class Signs(db.Model):
    __tablename__ = 'Signs'
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String)
    type = db.Column(db.String)
    dateStart = db.Column(db.Date)
    dateEnd = db.Column(db.Date)
    fileCertificate = db.Column(db.String)
    fileContainer = db.Column(db.String)
    issuer = db.Column(db.String)
    serial_number = db.Column(db.String)

    @property
    def leftdays(self):
        from datetime import date
        return int((self.dateEnd - date.today()).days)

    def __repr__(self):
        return '<Signs %r>' % self.id
