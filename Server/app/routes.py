from flask import url_for, redirect, request
from app import app
from flask_user import login_required, current_user
@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')
