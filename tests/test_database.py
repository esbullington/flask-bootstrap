from bs4 import BeautifulSoup
import unittest

from app.mod_users.models import User
from app import create_app, db, bcrypt

class DatabaseTestCase(unittest.TestCase):
    """ setup and teardown for testing the database """

    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        self.client = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_empty_db(self):
        total = db.session.query(User).count()
        assert total == 0

class AuthenticationTestCase(unittest.TestCase):
    """ setup and teardown for testing the database """

    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def login(self, username, password):
        return self.client.post('/users/login/', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_login_fail(self):
        res = self.login('randomuser', 'randompass')
        soup = BeautifulSoup(res.data)
        d = soup.find('span', 'flashdata')
        assert d.text == u'No such user. Please try again'

    def test_login_success(self):
        pw_hash = bcrypt.generate_password_hash('testpass')
        user = User(username='testuser', pw_hash=pw_hash)
        db.session.add(user)
        db.session.commit()
        res = self.login('testuser', 'testpass')
        soup = BeautifulSoup(res.data)
        d = soup.find('span', 'flashdata')
        assert d.text == u'Logged in successfully'

    def test_logout(self):
        res = self.client.get('/users/logout/', follow_redirects=True)
        soup = BeautifulSoup(res.data)
        d = soup.find('span', 'flashdata')
        assert d.text == u'User logged out'
