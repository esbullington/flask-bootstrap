from sqlalchemy import Column, Integer, String
import datetime
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # title = db.relationship('Title', backref = 'title', lazy = 'dynamic')
    first_name = db.Column(db.String(64), unique = True)
    last_name = db.Column(db.String(64), unique = True)
    middle_name = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    created_on = db.Column(db.DateTime)      

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

##########################################

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
          
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Title: %r>' % self.title
