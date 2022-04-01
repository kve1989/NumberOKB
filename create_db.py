from app import db
from app.models import *
from app.forms import tables
import random, math
from datetime import date

db.drop_all()
db.create_all()

i = 0
count_records = 30

while i < count_records:
    for table in tables:
        record = eval(table[0])(date=date.today(),
                                done=math.floor(random.random() * 100),
                                sent=math.floor(random.random() * 100),
                                mistakes=math.floor(random.random() * 100)
                            )

        db.session.add(record)
        db.session.commit()
    i += 1
