# manage.py
from flask_script import Shell, Manager
from flask import current_app

from app.database import db
from app.mod_users import models
from app import create_app

manager = Manager(create_app)

def _make_context():
    return dict(app=current_app, db=db, models=models)

manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command("shell", Shell(use_ipython=True, make_context=_make_context))

@manager.command
def createdb():
    db.init_app(current_app)
    db.create_all()

@manager.command
def dropdb():
    db.init_app(current_app)
    db.drop_all()

@manager.command
def testdb():
    from tests.test_database import DatabaseTestCase, AuthenticationTestCase
    import unittest
    runner = unittest.TextTestRunner()
    runner.run(unittest.makeSuite(DatabaseTestCase))
    runner.run(unittest.makeSuite(AuthenticationTestCase))

@manager.command
def testall():
    testdb()

if __name__ == "__main__":
    manager.run()
