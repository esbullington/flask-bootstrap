DB_OWNER="testuser"
DB_NAME="testdb"
DB_PASSWD="testpassword"
LOCAL_CFG=local.cfg

ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VENV_DIR=$(ROOT_DIR)/venv

install: system_depens create_virtualenv python_depens create_db create_cfg

# Sub-tasks

clean:
	@ rm -rf $(VENV_DIR)

print_dir:
	@ echo $(VENV_DIR)

system_depens:
	@ echo "Installing project's system dependencies..." && \
	sudo apt-get install postgresql python-pip python-dev libpq-dev python-virtualenv

create_virtualenv:
	@ echo "Installing Python virtual environment for project dependencies..." && \
	test -d $(VENV_DIR) || virtualenv $(VENV_DIR)

python_depens:
	. $(VENV_DIR)/bin/activate && \
	echo "Installing project's Python dependencies..." && \
	pip install -r requirements.txt

create_cfg:
	@ test -f $(LOCAL_CFG) || cat app.cfg > $(LOCAL_CFG) && \
	echo "SECRET_KEY = '"`cat /dev/urandom| tr -dc 'a-zA-Z0-9' | fold -w 32| head -n 1`"'" >> $(LOCAL_CFG)

remove_python_depens:
	. $(VENV_DIR)/bin/activate && \
	echo "Removing project's Python dependencies..." && \
	pip uninstall -r requirements.txt

create_db:
	@ sudo apt-get install -y postgresql && \
	echo "CREATE USER $(DB_OWNER) WITH PASSWORD '$(DB_PASSWD)';" | sudo -u postgres psql && \
	echo "CREATE DATABASE $(DB_NAME);" | sudo -u postgres psql && \
	echo "GRANT ALL PRIVILEGES ON DATABASE $(DB_NAME) to $(DB_OWNER);" | sudo -u postgres psql && \
	sudo service postgresql reload && \
	. $(VENV_DIR)/bin/activate && \
	python manage.py createdb

drop_db:
	@ echo "DROP DATABASE $(DB_NAME);" | sudo -u postgres psql && \
	echo "DROP USER $(DB_OWNER);" | sudo -u postgres psql && \
	sudo service postgresql reload

test:
	@ python manage.py testall

list:
	git ls-tree --full-tree -r HEAD

run:
	. $(VENV_DIR)/bin/activate && python app.py

.PHONY: install create_db python_depens system_depens create_virtualenv remove_python_depens drop_db
