# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from flask.ext.login import login_required

base = Blueprint('base', __name__, url_prefix='/', template_folder='base')

def index():
    return render_template('base/index.html')

# URLs
base.add_url_rule('/', 'index', index)
