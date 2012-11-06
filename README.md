# flask-bootstrap

Flask application framework pre-configured for SQL Alchemy, flask-auth authentication, and Twitter bootstrap frontend. Meant to serve as a skeleton application for you to customize as desired, not as a Flask extension.  If you are looking for a Flask extension that uses Flask blueprints, try the other [flask-bootstrap](https://github.com/mbr/flask-bootstrap).

## Install
    git clone git://github.com/esbullington/flask-bootstrap.git
    cd flask-bootstrap
    pip install -r requirements.txt


## Features

* Default templates with HTML5 Boilerplate included
* Base requirements.txt
* Bootstrap frontend framework from Twitter
* Pre-integrated with flask-auth, just create your postgres db and fill in app.cfg accordingly


##To Do 

* Set up default user authorization for admin user (authentication has already been setup using flask-auth)
* Integrate some sort of Python asset manager for static assets (i.e., JS/CSS minifier, file concatenator), ideally one that compiles CoffeeScript

