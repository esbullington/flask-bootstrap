# flask-bootstrap

Flask application framework pre-configured for SQL Alchemy, flask-auth authentication, and Twitter bootstrap frontend. Meant to serve as a skeleton application for you to customize as desired, not as a Flask extension.  If you are looking for a Flask extension that uses Flask blueprints, try the other [flask-bootstrap](https://github.com/mbr/flask-bootstrap).

## Install

The main system dependencies are Python, Postgreql, and their respective development packages

On Ubuntu or Debian, first install:

    sudo apt-get install postgresql python-dev libpq-dev

Red Hat, Fedora, and  other derivatives are said to require (confirmation would be welcome):

    yum install yum install postgresql-devel postgresql-libs libpqxx-devel

A brief article on getting these dependencies running on Windows (exact instructions would be welcome):

    http://initd.org/psycopg/articles/2011/06/05/psycopg-windows-mingw/

Once you have these installed on your system, the rest is simple:

    git clone git://github.com/esbullington/flask-bootstrap.git
    cd flask-bootstrap
    pip install -r requirements.txt
    
## Quickstart
* Install above dependencies
* Customize your app.cfg (renaming it would be a good idea)
* Get postgresql set up as outlined here: http://www.cyberciti.biz/faq/howto-add-postgresql-user-account/
* Then: `python app.py -c yourconfig.cfg`

## Features
* Base requirements.txt.
* Bootstrap 3.1 frontend framework from Twitter.
* Pre-integrated with flask-auth, just create your postgres db and fill in models and app.cfg accordingly.
* Existing user model and basic login/signup.

##To Do 
* Set up default user authorization for admin user (authentication has already been setup using flask-auth)
* Integrate some sort of Python asset manager for static assets (i.e., JS/CSS minifier, file concatenator)

