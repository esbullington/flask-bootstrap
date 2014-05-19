# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from models import database
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.auth import Auth, AuthUser, login_required, logout
from models.sa import get_user_class

app = Flask(__name__)
app.config.from_pyfile('local.cfg')

# Instantiate and start DB
db = SQLAlchemy(app)
db_session = database.init_db(app.config.get('SQLALCHEMY_DATABASE_URI'))

## Set SQL Alchemy to automatically tear down
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

# Instantiate authentication
auth = Auth(app, login_url_name='login')
User = get_user_class(db.Model)

def index():
    return render_template('index.html')

##login methods

def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter(User.username==username).first()
        if user is not None:
            # Authenticate and log in!
            if user.authenticate(request.form['password']):
                session['username'] = request.form['username']
                return redirect(url_for('home'))
            else:
                flash('Incorrect password. Please try again')
                return render_template('login.html')
        else:
            session['username'] = None
            flash('Incorrect username. Please try again')
            return render_template('login.html')
    return render_template('login.html')

@login_required()
def home():
    ##Dump variables in templates
    return render_template('home.html')

def user_create():
    if request.method == 'POST':
        username = request.form['username']
        if User.query.filter(User.username==username).first():
            return 'User already exists.'
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('user_create.html')

def logout_view():
    user_data = logout()
    session['username'] = None
    if user_data is None:
        msg = 'No user to log out.'
        return render_template('logout.html', msg=msg)
    else:
        msg = 'Logged out user {0}.'.format(user_data['username'])
        return render_template('logout.html', msg=msg)

# URLs
app.add_url_rule('/', 'index', index)
app.add_url_rule('/login/', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/home/', 'home', home)
app.add_url_rule('/users/create/', 'user_create', user_create, methods=['GET', 'POST'])
app.add_url_rule('/logout/', 'logout', logout_view)

# Secret key needed to use sessions.
app.secret_key = app.config['SECRET_KEY']
  
if __name__ == "__main__":
    print "Host ip is: " + app.config['HOST_IP']
    app.run(debug=app.config.get('DEBUG'), host=app.config.get('HOST_IP'))
