# -*- coding: utf-8 -*-
from flask import request, make_response, render_template, flash, redirect, url_for, session, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from app.models.user import User, ROLE_USER, ROLE_ADMIN
from app.database import db, bcrypt

# Instantiate login
login_manager = LoginManager()
login_manager.login_view = 'login'

# Load user into each response
@login_manager.user_loader
def load_user(id):
        return User.query.get(int(id))

##login views
def login_view():
    if request.method == 'GET':
        return render_template('login.html')
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('home'))
    username = request.form['username']
    user = User.query.filter(User.username==username).first()
    if user is None:
        flash('No such user. Please try again')
        return render_template('login.html')
    pw_check = bcrypt.check_password_hash(user.pw_hash, request.form['password'])
    if not pw_check:
        flash('Incorrect password. Please try again')
        return render_template('login.html')
    login_user(user)
    flash("Logged in successfully")
    return redirect(url_for('home'))

def user_create():
    if request.method == 'POST':
        username = request.form['username']
        if User.query.filter(User.username==username).first():
            flash('User already exists. Please log in.')
            return redirect(url_for('login'))
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        user = User(username=username, pw_hash=pw_hash)
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered. Please log in.')
        return redirect(url_for('login'))
    return render_template('user_create.html')

def logout_view():
    logged_out_msg = 'Logged out user {0}'.format(g.user.username)
    logged_out = logout_user()
    session['username'] = None
    if logged_out:
        return render_template('logout.html', msg=logged_out_msg)
    msg = 'No user to log out.'
    return render_template('logout.html', msg=msg)
