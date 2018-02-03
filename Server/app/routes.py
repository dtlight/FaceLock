from flask import render_template, url_for, redirect, request
from app import app, db, models
from flask_user import login_required, current_user
from app.models import User
@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/logs')
def home():
    return render_template('logs.html')

@app.route('/settings')
def home():
    return render_template('settings.html')

@app.route('/unlock')
def home():
    return render_template('unlock.html')
