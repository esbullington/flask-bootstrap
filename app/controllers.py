# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from flask.ext.login import login_required


def index():
    return render_template('index.html')

@login_required
def home():
    ##Dump variables in templates
    return render_template('home.html')
