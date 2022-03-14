from ..app import db
from ..app.models import ProtocConsult
import random, math
from datetime import today

count_records = 30

for i in count_records:
    record = ProtocConsult(date=today(),
                            done=math.floor(random.random() * 10),
                            sent=math.floor(random.random() * 10),
                            mistakes=math.floor(random.random() * 10),
                        )

    db.session.add(record)
    db.session.commit()