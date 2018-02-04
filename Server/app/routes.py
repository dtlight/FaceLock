from flask import render_template, url_for, redirect, request, abort
from app import app, db, models
from flask_user import login_required, current_user
from app.models import User
from werkzeug.utils import secure_filename
import json
import base64
import os
from app.forms import LoginForm

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    form = LoginForm()
    if form.validate_on_submit():
    	if form.username.data == "admin":
            admin = db.session.query(User).filter_by(username="admin").all()
            admin_pw = admin[0].password        
            if admin_pw == form.password.data:
                     
                return redirect(url_for('settings'))

    return render_template('login.html', title='Sign In', form=form)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

@app.route('/settings', methods=["GET"])
def settings():
    return render_template('settings.html')

@app.route('/unlock')
def unlock():
    return render_template('unlock.html')


@app.route('/pi', methods=["GET", "POST"])
def parse_request():
    if request.json:
        img = request.get_json()
        image_64_decode = ''
        for key in img: 
            image_64_decode = base64.b64decode(img[key])
            abspath = os.path.abspath(os.path.dirname(__file__))
            image_result = open(abspath + '/static/images/image.jpg','wb')
            image_result.write(image_64_decode)
        
    if request.method == 'GET':
        return '<img src="' + url_for('static', filename='images/image.jpg') + '">'
