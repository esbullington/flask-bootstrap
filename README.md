Flask-Bootstrap
=========
Flask-Bootstrap is an Flask app template for users to clone and customize as desired, as opposed to a Flask extension that you can install and use in your existing application.

----
This version of Flask-Bootstrap app template, v0.2.0, is a distinctly different version of the prior flask application template, now better organized using [Flask blueprints](http://flask.pocoo.org/docs/0.10/blueprints/).  I think users will find this version much better suited for anything larger than the very smallest of server-side web apps.

Nonetheless, in the event that you'd like to use the old flask-bootstrap template, that version can now be found in the `old_master` branch.

----

Features
----
  - Flask, including Flask-SQLAlchemy for user data and Flask-Login for authentication
  - Bootstrap 3
  - Webassets for easy Javascript deployment
  - Targeting OWASP web security standards
  - Python 2 and 3 support

Version
----
0.2.1

[![Build Status](https://travis-ci.org/esbullington/flask-bootstrap.svg?branch=master)](https://travis-ci.org/esbullington/flask-bootstrap)

Quickstart
----
* Install the [system dependencies](#1-system-dependencies) and [Python dependencies](#2-python-virtual-environment-and-dependencies)
* Customize your `config/app.cfg` (`make create_cfg` creates a basic `config/local.cfg`)
* Fill out appropriate `Makefile` variables and run `make`
* Then: `python run.py` or `make run`

Full installation instructions
----
The main system dependencies are Python, Postgreql, and their respective development packages.  It could be easily adapted to run on MySQL or even SQLite, but the default installation instructions and Makefile below assume the use of PostgreSQL.

#### Makefile
If you're on Ubuntu or Mint and you using Make, you're in luck. There is a very convenient Makefile to install and run the application (should work with Debian with a few minor changes).  If you wish to use the Makefile, then simply fill in the appropriate config variables in the Makefile, run `make install` to install dependencies, and `make run` to start the application.  The Makefile installation will even create a default `local.cfg` containing your project's configuration, for you to use and customize.

Otherwise, refer to the instructions below.

#### 1. System dependencies: 
On Ubuntu or Debian, first install:

    sudo apt-get install postgresql python-dev libpq-dev

Red Hat, Fedora, and  other derivatives are said to require (confirmation would be welcome):

    yum install postgresql-devel postgresql-libs libpqxx-devel

Here's a [brief article](http://initd.org/psycopg/articles/2011/06/05/psycopg-windows-mingw/) on getting these dependencies running on Windows (exact instructions would be welcome).

#### 2. Python virtual environment and dependencies
It's probably a good idea to create a virtual environment for this project using `virtualenv` and `virtualenvwrapper`, which are installed using:

    pip install virtualenvwrapper

Then, clone the repo, cd into it, and create a project virtual environment.  I like to host my virtual environments in each project directory (but include it in the .gitignore so it's not gitable). So something like:

    git clone git://github.com/esbullington/flask-bootstrap.git
    cd flask-bootstrap
    virtualenv venv
    source venv/bin/activate

Once you have the virtual environment installed on your system, and the system dependencies, the rest is simple:

    pip install -r config/requirements.txt

Configuration
----
* If you're using the Makefile, be sure to set your config filename
* Otherwise, you can either:
  - pass your config file using `python manage.py -c config/yourconfig.cfg runserver` or else
  - set an environmental variable `FLASK_APPLICATION_SETTINGS` to point to your config file
* Check to be sure your `SECRET_KEY` config setting is indeed secret and cryptographically strong (120+ bits of entropy)
* The Makefile command `make create_cfg` sets this `SECRET_KEY` automatically as part of the config creation

Tests
----
`make test` or `python manage.py testall`

Master:

[![Build Status](https://travis-ci.org/esbullington/flask-bootstrap.svg?branch=master)](https://travis-ci.org/esbullington/flask-bootstrap)

Dev:

[![Build Status](https://travis-ci.org/esbullington/flask-bootstrap.svg?branch=development)](https://travis-ci.org/esbullington/flask-bootstrap)

Changelog
----
####v0.2.1
* Added filler template pages, including user settings page
* Reorganized module naming (`mod_home`->`mod_unauthenticated`)
* Restyled Bootstrap in homepage and navbar

####v0.2.0
* Flask Blueprints
* Flask-assets asset for Javascript and other static assets, based on the webassets module
* CSRF protection

Roadmap
----
* For v0.3.0
    - More unit tests for Flask app and JavaScript
    - Automated app naming through Flask-Script or Makefile
    - Add more and better documentation, using Sphinx
    - More attractive user interface
* By version 1.0.0
    - Comprehensive security review and tests using OWASP standards
    - Full Windows and OSX support

License
----

BSD
