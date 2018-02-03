from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_user import SQLAlchemyAdapter, UserManager

app = Flask(__name__)
app.static_folder = 'static'

app.config.from_object(Config)


