# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from flask.ext.login import login_required

home = Blueprint('home', __name__, url_prefix='/', template_folder='home')

# Add CSS sheet only for unauthenticated urls
@home.context_processor
def css_processor():
    return dict(css_file='/static/css/outer.css')

def index():
    return render_template('home/index.html')

# URLs
home.add_url_rule('/', 'index', index)
