from app import db
from app.forms import tables
from app.models import TablesInCurrentBase

db.drop_all()

# Create DB
db.create_all()

# Filling the database
for table in tables:
    record = TablesInCurrentBase(name=table[0], description=table[1])
    db.session.add(record)
    db.session.commit()