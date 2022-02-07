from app import db

# 1. Протокол консультации
class ProtocConsult(db.Model):
    __tablename__ = '1.ProtocConsult'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<ProtocConsult %r>' % self.id

# 2. Контрольная карта диспансеризации
class ProfMedicalExam(db.Model):
    __tablename__ = '2.ProfMedicalExam'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<ProfMedicalExam %r>' % self.id

# 3. Лабораторные исследования
class LabResearch(db.Model):
    __tablename__ = '3.LabResearch'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<LabResearch %r>' % self.id

# 4. Медицинские свидетельства о рождении
class MedCertBirth(db.Model):
    __tablename__ = '4.MedCertBirth'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<MedCertBirth %r>' % self.id

# 5. Направление на МСЭ
class DirectionOnMCE(db.Model):
    __tablename__ = '5.DirectionOnMCE'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<DirectionOnMCE %r>' % self.id

# 6. Направление на МСЭ
class DirectionOnMCE(db.Model):
    __tablename__ = '6.DirectionOnMCE'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<DirectionOnMCE %r>' % self.id

# 7. Протокол инструментальных исследований
class DirectionOnMCE(db.Model):
    __tablename__ = '7.ProtocInstrumentStudies'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<ProtocInstrumentStudies %r>' % self.id

# 8. Молочная смесь
class MilkMixture(db.Model):
    __tablename__ = '8.MilkMixture'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<MilkMixture %r>' % self.id

# 9. Рецепты
class Recipes(db.Model):
    __tablename__ = '9.Recipes'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<Recipes %r>' % self.id

# 10. Статкарта
class Statcard(db.Model):
    __tablename__ = '10.Statcard'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<Statcard %r>' % self.id

# 11. Экстренное извещение
class EmergencyNotice(db.Model):
    __tablename__ = '11.EmergencyNotice'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<EmergencyNotice %r>' % self.id

# 12. Эпикриз Выписка из медицинской документации пациента
class EpicrisisExtrFromPatientsMedRecs(db.Model):
    __tablename__ = '12.EpicrisisExtrFromPatientsMedRecs'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer)
    sent = db.Column(db.Integer)
    mistakes = db.Column(db.Integer)

    def __repr__(self):
        return '<EpicrisisExtrFromPatientsMedRecs %r>' % self.id






















class PCR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=False)
    sent = db.Column(db.Integer, nullable=False)
    mistakes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<PCR %r>' % self.id