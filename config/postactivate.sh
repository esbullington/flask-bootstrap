# an example of setting environment variables for a django project to your virtual env
echo "# This hook is run after this virtualenv is activated.
export FLASK_APPLICATION_SETTINGS=$VIRTUAL_ENV/../config/local.cfg" >> $VIRTUAL_ENV/bin/activate
