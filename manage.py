#!/usr/bin/env python

from __future__ import absolute_import

from flaskext.script import Manager

from app import app


manager = Manager(app)

if __name__ == "__main__":
    manager.run()
