# flask-bootstrap

Flask application framework pre-configured for SQL Alchemy, flask-auth authentication, and Twitter bootstrap frontend. Meant to serve as a skeleton application for you to customize as desired, not as a Flask extension.
Based on [Flask Tool's](https://github.com/imlucas/flask-tool) simple app template by [imlucas](http://www.imlucas.com/) and Twitter's [Bootstrap framework](http://twitter.github.com/bootstrap/).

## Install
    git clone git://github.com/esbullington/flask-bootstrap.git
    cd flask-bootstrap
    pip install -r requirements.txt

## Run the app locally


## Deploy to AWS

Change the appropriate settings in fabfile.py and 
    fab deploy


## Features

* Default templates with HTML5 Boilerplate included
* Ready to go manage.py that uses the excellent Flask-Script package
* Supervisord config to run your app on uwsgi
* Nginx config and required dependencies
* Pre built fabfile for deployment on ec2 via Fabric
* Base requirements.txt
* Bootstrap frontend framework from Twitter


##TO DO 

* Set up default user authorization for admin user (authentication has already been setup using flask-auth)
* Integrate some sort of Python asset manager for static assets (i.e., JS/CSS minifier, file concatenator), ideally one that compiles CoffeeScript

