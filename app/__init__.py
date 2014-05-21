# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from app.database import db, bcrypt
from app.controllers import index, home
from app.login import login_manager, login_view, logout_view, user_create
import os

def create_app(config=None):

    app = Flask(__name__)


    # If no config file is passed in on the command line:
    if config is None:
        config = os.path.join(app.root_path, '../config/example.cfg')

    app.config.from_pyfile(config)

    # In case you don't wish to include them in your config file,
    # These variables can be set in your local environment
    # if app.config.get('SQLALCHEMY_DATABASE_URI') is None:
    #     app.config.from_envvar('SQLALCHEMY_DATABASE_URI')
    # if app.config.get('SECRET_KEY') is None:
    #     app.config.from_envvar('SECRET_KEY')

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
