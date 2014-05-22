# manage.py
from flask.ext.script import Shell, Manager

from app.database import db
from app import models
from app import create_app


def _make_context():
    return dict(app=create_app, db=db, models=models)

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command("shell", Shell(use_ipython=True, make_context=_make_context))

@manager.command
def createdb():
    app = create_app()
    db.init_app(app)
    db.create_all()

@manager.command
def dropdb():
    app = create_app()
    db.init_app(app)
    db.drop_all()

@manager.command
def testdb():
    from tests.test_database import DatabaseTestCase
    import unittest
    runner = unittest.TextTestRunner()
    runner.run(unittest.makeSuite(DatabaseTestCase))

@manager.command
def testall():
    testdb()

if __name__ == "__main__":
    manager.run()
