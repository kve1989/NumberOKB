import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '01f260718007c0bd2ef3e9005b84ab97'
