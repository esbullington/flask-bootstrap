# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Instantiate and start DB
db = SQLAlchemy()

# Likewise with Bcrypt extension
bcrypt = Bcrypt()
