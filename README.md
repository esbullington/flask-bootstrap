# flask-bootstrap

Flask application framework pre-configured for SQL Alchemy, flask-auth authentication, and Twitter bootstrap frontend. Meant to serve as a skeleton application for you to customize as desired, not as a Flask extension.  If you are looking for a Flask extension that uses Flask blueprints, try the other [flask-bootstrap](https://github.com/mbr/flask-bootstrap).

## Install
    git clone git://github.com/esbullington/flask-bootstrap.git
    cd flask-bootstrap
    pip install -r requirements.txt


## Features

* Base requirements.txt.
* Bootstrap 3.1 frontend framework from Twitter.
* Pre-integrated with flask-auth, just create your postgres db and fill in models and app.cfg accordingly.
* Existing user model and basic login/signup.


##To Do 
* Set up default user authorization for admin user (authentication has already been setup using flask-auth)
* Integrate some sort of Python asset manager for static assets (i.e., JS/CSS minifier, file concatenator).

