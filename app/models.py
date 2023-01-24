from app import db


# 1. Протокол консультации
class ProtocConsult(db.Model):
    __tablename__ = '1.ProtocConsult'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<ProtocConsult %r>' % self.id


# 2. Контрольная карта диспансеризации
class ProfMedicalExam(db.Model):
    __tablename__ = '2.ProfMedicalExam'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<ProfMedicalExam %r>' % self.id


# 3. Лабораторные исследования
class LabResearch(db.Model):
    __tablename__ = '3.LabResearch'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<LabResearch %r>' % self.id


# 4. Медицинские свидетельства о рождении
class MedCertBirth(db.Model):
    __tablename__ = '4.MedCertBirth'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<MedCertBirth %r>' % self.id


# 5. Направление на МСЭ
class DirectionOnMCE(db.Model):
    __tablename__ = '5.DirectionOnMCE'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<DirectionOnMCE %r>' % self.id


# 6. Направление на госпитализацию, восстановительное лечение, обследование, консультацию
class DirectToHospRehabExamCons(db.Model):
    __tablename__ = '6.DirectToHospRehabExamCons'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<DirectToHospRehabExamCons %r>' % self.id


# 7. Протокол инструментальных исследований
class ProtocInstrumentStudies(db.Model):
    __tablename__ = '7.ProtocInstrumentStudies'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<ProtocInstrumentStudies %r>' % self.id


# 8. Молочная смесь
class MilkMixture(db.Model):
    __tablename__ = '8.MilkMixture'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<MilkMixture %r>' % self.id


# 9. Рецепты
class Recipes(db.Model):
    __tablename__ = '9.Recipes'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<Recipes %r>' % self.id


# 10. Статкарта
class Statcard(db.Model):
    __tablename__ = '10.Statcard'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<Statcard %r>' % self.id


# 11. Экстренное извещение
class EmergencyNotice(db.Model):
    __tablename__ = '11.EmergencyNotice'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<EmergencyNotice %r>' % self.id


# 12. Эпикриз Выписка из медицинской документации пациента
class EpicrisisExtrFromPatientsMedRecs(db.Model):
    __tablename__ = '12.EpicrisisExtrFromPatientsMedRecs'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<EpicrisisExtrFromPatientsMedRecs %r>' % self.id


# 13. Эпикриз взятия на Д учет
class EpicrisisDaccounting(db.Model):
    __tablename__ = '13.EpicrisisDaccounting'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<EpicrisisDaccounting %r>' % self.id


# 14. Эпикриз выписной
class EpicrisisDischarge(db.Model):
    __tablename__ = '14.EpicrisisDischarge'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<EpicrisisDischarge %r>' % self.id


# 15. Эпикриз переводной
class EpicrisisTranslation(db.Model):
    __tablename__ = '15.EpicrisisTranslation'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<EpicrisisTranslation %r>' % self.id


# 16. Эпикриз посмертный
class EpicrisisPosthumous(db.Model):
    __tablename__ = '16.EpicrisisPosthumous'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<EpicrisisPosthumous %r>' % self.id


# 17. Эпикриз предоперационный
class EpicrisisPreoperative(db.Model):
    __tablename__ = '17.EpicrisisPreoperative'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<EpicrisisPreoperative %r>' % self.id


# 18. Эпикриз снятия с Д учета
class EpicrisisDremoval(db.Model):
    __tablename__ = '18.EpicrisisDremoval'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<EpicrisisDremoval %r>' % self.id


# 19. Эпикриз этапный
class EpicrisisStage(db.Model):
    __tablename__ = '19.EpicrisisStage'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<EpicrisisStage %r>' % self.id


# 20. Вакцинация (вся)
class VaccinationAll(db.Model):
    __tablename__ = '20.Vaccination(all)'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<VaccinationAll %r>' % self.id


# 21. Вакцинация (Covid)
class VaccinationCovid(db.Model):
    __tablename__ = '21.Vaccination(Covid)'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<VaccinationCovid %r>' % self.id


# 22. Вызов врача на дом
class CallDocAtHome(db.Model):
    __tablename__ = '22.CallDocAtHome'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<CallDocAtHome %r>' % self.id


# 23. Сведения о смерти
class DeathInform(db.Model):
    __tablename__ = '23.DeathInform'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<DeathInform %r>' % self.id


# 24. Сведения о перинатальной смерти
class InformPerinatalDeath(db.Model):
    __tablename__ = '24.InformPerinatalDeath'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<InformPerinatalDeath %r>' % self.id


# 25. ЭЛН открытых
class ELNOpen(db.Model):
    __tablename__ = '25.ELN(open)'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<ELNOpen %r>' % self.id


# 26. ЭЛН открытых
class ELNClose(db.Model):
    __tablename__ = '26.ELN(close)'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<ELNClose %r>' % self.id


# 27. Лабораторные исследования (ПЦР)
class LabResPCR(db.Model):
    __tablename__ = '27.LabResPCR'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    done = db.Column(db.Integer, nullable=True, default=0)
    sent = db.Column(db.Integer, nullable=True, default=0)
    mistakes = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<LabResPCR %r>' % self.id

# Электронно-цифровые подписи
class Signs(db.Model):
    __tablename__ = 'Signs'
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String)
    type = db.Column(db.String)
    dateStart = db.Column(db.Date)
    dateEnd = db.Column(db.Date)
    fileCertificate = db.Column(db.String)
    fileContainer = db.Column(db.String)

    def __repr__(self):
        return '<Signs %r>' % self.id