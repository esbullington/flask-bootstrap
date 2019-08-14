# -*- coding: utf-8 -*-
from flask import Blueprint, request, make_response, render_template, flash, redirect, url_for, session, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_wtf.csrf import CSRFProtect

from .models import User, ROLE_USER, ROLE_ADMIN
from app.database import db, bcrypt


# Define the blueprint: 'auth', set its url prefix: app.url/auth
users = Blueprint('users', __name__, url_prefix='/users')

# Protect against CSRF attacks
csrf = CSRFProtect()

# Instantiate login
login_manager = LoginManager()
login_manager.login_view = 'login'

# Load user into each response
@login_manager.user_loader
def load_user(id):
        return User.query.get(int(id))

##login views
def login():
    if request.method == 'GET':
        return render_template('users/login.html')
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('authenticated.index'))
    username = request.form['username']
    user = User.query.filter(User.username==username).first()
    if user is None:
        flash('No such user. Please try again')
        return render_template('users/login.html')
    pw_check = bcrypt.check_password_hash(user.pw_hash, request.form['password'])
    if not pw_check:
        flash('Incorrect password. Please try again')
        return render_template('users/login.html')
    login_user(user)
    flash("Logged in successfully")
    return redirect(url_for('authenticated.index'))

def register():
    if request.method == 'POST':
        username = request.form['username']
        if User.query.filter(User.username==username).first():
            flash('User already exists. Please log in.')
            return redirect(url_for('users.login'))
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        user = User(username=username, pw_hash=pw_hash)
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered. Please log in.')
        return redirect(url_for('users.login'))
    return render_template('users/register.html')

def logout():
    logged_out = logout_user()
    if logged_out:
        msg = 'User logged out'
        flash(msg)
        return render_template('users/logout.html', msg=msg)
    msg = 'No user to log out.'
    flash(msg)
    return render_template('users/logout.html', msg=msg)

@login_required
def settings():
    return render_template('users/settings.html')

# URLs
users.add_url_rule('/login/', 'login', login, methods=['GET', 'POST'])
users.add_url_rule('/register/', 'register', register, methods=['GET', 'POST'])
users.add_url_rule('/settings/', 'settings', settings)
users.add_url_rule('/logout/', 'logout', logout)
