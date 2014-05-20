# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

# Instantiate and start DB
db = SQLAlchemy()

# Likewise with Bcrypt extension
bcrypt = Bcrypt()
