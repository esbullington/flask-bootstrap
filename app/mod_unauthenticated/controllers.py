# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from flask_login import login_required

unauthenticated = Blueprint('unauthenticated', __name__, template_folder='unauthenticated')

# Add CSS sheet only for unauthenticated urls
@unauthenticated.context_processor
def css_processor():
    return dict(css_file='/static/css/unauthenticated.css')

def index():
    return render_template('unauthenticated/index.html')

def about():
    return render_template('unauthenticated/about.html')

# URLs
unauthenticated.add_url_rule('/about/', 'about', about)
unauthenticated.add_url_rule('/', 'index', index)
