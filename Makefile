DB_OWNER="testuser"
DB_NAME="testdb"
DB_PASSWD="testpassword"
LOCAL_CFG=local.cfg
HOST=0.0.0.0

ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VENV_DIR=$(ROOT_DIR)/venv

install: system_depens create_virtualenv create_cfg python_depens create_db

# Sub-tasks

clean:
	@ rm -rf $(VENV_DIR) && find . -name "*.pyc" -type f -delete

print_dir:
	@ echo $(VENV_DIR)

shell:
	@ python manage.py shell

system_depens:
	@ echo "Installing project's system dependencies..." && \
	sudo apt-get install postgresql python-pip python-dev libpq-dev python-virtualenv

create_virtualenv:
	@ echo "Installing Python virtual environment for project dependencies..." && \
	test -d $(VENV_DIR) || virtualenv $(VENV_DIR) && \
	. $(VENV_DIR)/bin/activate && \
	/bin/bash config/postactivate.sh

python_depens:
	. $(VENV_DIR)/bin/activate && \
	echo "Installing project's Python dependencies..." && \
	pip install -r config/requirements.txt

create_cfg:
	@ test -f config/$(LOCAL_CFG) || cat config/example.cfg > config/$(LOCAL_CFG) && \
	echo "SQLALCHEMY_DATABASE_URI='postgresql://$(DB_OWNER):$(DB_PASSWD)@127.0.0.1/$(DB_NAME)'" >> config/$(LOCAL_CFG) && \
	echo "SECRET_KEY = '"`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1`"'" >> config/$(LOCAL_CFG)

remove_python_depens:
	. $(VENV_DIR)/bin/activate && \
	echo "Removing project's Python dependencies..." && \
	pip uninstall -r config/requirements.txt

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
	. $(VENV_DIR)/bin/activate && python manage.py -c ../config/$(LOCAL_CFG) runserver --host $(HOST)

.PHONY: install create_db python_depens system_depens create_virtualenv remove_python_depens drop_db run list shell
