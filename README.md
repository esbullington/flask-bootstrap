# flask-bootstrap

[![Build Status](https://travis-ci.org/esbullington/flask-bootstrap.svg?branch=master)](https://travis-ci.org/esbullington/flask-bootstrap)

Flask application framework pre-configured for SQL Alchemy, flask-login, and Twitter bootstrap frontend. Meant to serve as a skeleton application for you to customize as desired, not as a Flask extension.

If you are looking for a Flask extension that uses Flask blueprints to provide Bootstrap support, try the other [flask-bootstrap](https://github.com/mbr/flask-bootstrap).

## Install
The main system dependencies are Python, Postgreql, and their respective development packages.  It could be easily adapted to run on MySQL or even SQLite, but the default installation instructions and Makefile below assume the use of PostgreSQL.

#### Makefile
If you're on Ubuntu or Mint and you using Make, you're in luck. There is a very convenient Makefile to install and run the application (should work with Debian with a few minor changes).  If you wish to use the Makefile, then simply fill in the appropriate config variables in the Makefile, run `make install` to install dependencies, and `make run` to start the application.  The Makefile installation will even create a default `local.cfg` containing your project's configuration, for you to use and customize.

Otherwise, refer to the instructions below.

#### 1. System dependencies: 
On Ubuntu or Debian, first install:

    sudo apt-get install postgresql python-dev libpq-dev

Red Hat, Fedora, and  other derivatives are said to require (confirmation would be welcome):

    yum install yum install postgresql-devel postgresql-libs libpqxx-devel

Here's a [brief article](http://initd.org/psycopg/articles/2011/06/05/psycopg-windows-mingw/) on getting these dependencies running on Windows (exact instructions would be welcome)

#### 2. Python virtual environment and dependencies
It's probably a good idea to create a virtual environment for this project:
    pip install virtualenv
Then, create a project virtual environment.  I like to host my virtual environments in each project directory (but include it in the .gitignore so it's not gitable). So something like:

    virtualenv venv
    source venv/bin/activate

Once you have the virtual environment installed on your system, and the system dependencies, the rest is simple:

    git clone git://github.com/esbullington/flask-bootstrap.git
    cd flask-bootstrap
    pip install -r requirements.txt

    
## Quickstart
* Install above dependencies
* Customize your `app.cfg` (`local.cfg` would be a good name)
* Get postgresql set up as outlined here: http://www.cyberciti.biz/faq/howto-add-postgresql-user-account/
* Then: `python app.py` or `make run`

## Tests
`make test` or `python manage.py testall`

Master:
[![Build Status](https://travis-ci.org/esbullington/flask-bootstrap.svg?branch=master)](https://travis-ci.org/esbullington/flask-bootstrap)

Dev:
[![Build Status](https://travis-ci.org/esbullington/flask-bootstrap.svg?branch=development)](https://travis-ci.org/esbullington/flask-bootstrap)

## Features
* Base requirements.txt.
* Bootstrap 3.1 frontend framework from Twitter.
* Pre-integrated with flask-login, just create your postgres db and fill in models and app.cfg accordingly.
* Existing user model and basic login/signup.

##Roadmap
* For v0.0.2 release (imminent)
    - More unit tests for Flask app and JavaScript
    - Coherent organization of CSS assets
    - Flask-WTF support
* For v0.0.3 (April 2014)
    - Integrate some sort of Python asset manager for static assets (i.e., JS/CSS minifier, file concatenator)
    - Automated app naming through Flask-Script or Makefile
    - Add more and better documentation, using Sphinx and mitsuhiko/flask-sphinx-themes
    - Comprehensive security review and tests using OWASP standards
