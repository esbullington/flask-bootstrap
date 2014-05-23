import unittest
from app.models import User
from app import create_app, db


class DatabaseTestCase(unittest.TestCase):
    """ setup and teardown for testing the database """

    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def login(self, username, password):
        return self.client.post('/login/', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/logout/', follow_redirects=True)

    def test_empty_db(self):
        total = db.session.query(User).count()
        assert total == 0

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data
