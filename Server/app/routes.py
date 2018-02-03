from flask import render_template, url_for, redirect, request
from app import app, db, models
from flask_user import login_required, current_user
from app.models import User
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/unlock')
def unlock():
    return render_template('unlock.html')


@app.route('/piTest', methods=["POST"])
def method():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("1234")
        return "HELLO"
