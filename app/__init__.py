# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from app.database import db, bcrypt

from app.base.controllers import index, home

# from app.users.forms import RegisterForm, LoginForm
from app.users.login import login_manager, login_view, logout_view, user_create
from app.users.models import User
from app.users.decorators import requires_login

import os

def create_app(config=None):

    app = Flask(__name__)


    # If no config file is passed in on the command line:
    if config is None:
        config = os.path.join(app.root_path, os.environ.get('FLASK_APPLICATION_SETTINGS'))

    app.config.from_pyfile(config)

    # Secret key needed to use sessions.
    app.secret_key = app.config['SECRET_KEY']

    # Initialize SQL Alchemy and Flask-Login
    # Instantiate the Bcrypt extension
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Automatically tear down SQLAlchemy
    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

    @app.before_request
    def before_request():
        g.user = current_user

    # URLs
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/login/', 'login', login_view, methods=['GET', 'POST'])
    app.add_url_rule('/home/', 'home', home)
    app.add_url_rule('/users/create/', 'user_create', user_create, methods=['GET', 'POST'])
    app.add_url_rule('/logout/', 'logout', logout_view)

    return app
