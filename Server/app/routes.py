from flask import render_template, url_for, redirect, request
from app import app
from flask_user import login_required, current_user
@app.route('/')
@app.route('/index')
def index():
    return render_template('test.html')
