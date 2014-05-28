# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from flask.ext.login import login_required


def index():
    return render_template('index.html')

@login_required
def home():
    ##Dump variables in templates
    return render_template('home.html')

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
