import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "this is very very secret"
    SQLALCHEMY_DATABASE_URI = os.environ.get("CODEZILLA_DATABASE_URL") or "sqlite:///"+ os.path.join(basedir,"app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False