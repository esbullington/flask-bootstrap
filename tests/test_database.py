import unittest
from app.models import User
from app import create_app, db


class DatabaseTestCase(unittest.TestCase):
    """ setup and teardown for testing the database """

    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_empty_db(self):
        total = db.session.query(User).count()
        assert total == 1
