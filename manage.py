# manage.py

from flask.ext.script import Manager

from app.database import db
from app import app

manager = Manager(app)

@manager.command
def createdb():
    db.init_app(app)
    db.create_all()

@manager.command
def dropdb():
    db.init_app(app)
    db.drop_all()

if __name__ == "__main__":
    manager.run()
