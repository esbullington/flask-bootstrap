# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_assets import Environment, Bundle

from app.database import db, bcrypt
from app.mod_unauthenticated.controllers import unauthenticated
from app.mod_authenticated.controllers import authenticated
from app.mod_users.controllers import users, login_manager, csrf

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

    # CSRF protection
    csrf.init_app(app)

    # Web assets (js, less)
    assets = Environment(app)
    js = Bundle('js/main.js',
                filters='jsmin', output='gen/bundle.js')
    assets.register('js_all', js)

    # Automatically tear down SQLAlchemy
    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

    @app.before_request
    def before_request():
        g.user = current_user

    app.register_blueprint(unauthenticated)
    app.register_blueprint(authenticated)
    app.register_blueprint(users)

    return app
