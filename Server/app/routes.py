from flask import render_template, url_for, redirect, request
from app import app, db, models
from flask_user import login_required, current_user
from app.models import User
@app.route('/')
@app.route('/index')
def index():
    print(User.query.all())
    return render_template('login.html')

@app.route('/test')
def test():
	u = User.query.get(1)
	print(u)
	return u.username

