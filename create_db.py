from app import db
from app.models import *
from app.forms import tables
import random, math
from datetime import date

db.drop_all()
db.create_all()