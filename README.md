# flask-bootstrap

Flask application framework pre-configured for SQL Alchemy, flask-auth authentication, and Twitter bootstrap frontend.
Based on Flask Tool's simple app template by imlucas and Twitter's bootstrap framework.

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



