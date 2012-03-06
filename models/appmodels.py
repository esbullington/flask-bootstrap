from sqlalchemy import Column, Integer, String
from database import Base
import datetime
from app import db


##########################################

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    middle_initial = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50))
    created_on = db.Column(db.DateTime)      
    student = db.Column(db.String(50))
    
    def __init__(self, title):
        self.title = title
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.student_class = student_class
        self.email = mail
        if created_on is None:
            created_on = datetime.utcnow()
        self.created_on = created_on

    def __repr__(self):
        return '<Contact: %r>' % self.last_name


##########################################

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
          
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Title: %r>' % self.title
