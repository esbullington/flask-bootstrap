# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from flask_login import login_required

authenticated = Blueprint('authenticated', __name__, url_prefix='/authenticated', template_folder='authenticated')

# Add CSS sheet only for unauthenticated urls
@authenticated.context_processor
def css_processor():
    return dict(css='/static/css/authenticated.css')

@login_required
def index():
    return render_template('authenticated/index.html')

# URLs
authenticated.add_url_rule('/home/', 'index', index)
