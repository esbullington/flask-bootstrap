import unittest
from app.models import User
from app import app, db


class DatabaseTestCase(unittest.TestCase):
    """ setup and teardown for testing the database """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testuser:testpassword@127.0.0.1/testdb'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_empty_db(self):
        total = db.session.query(User).count()
        assert total == 0
