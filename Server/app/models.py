from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    profile = db.relationship('Profile', backref='user', lazy=True, uselist=False)
    log = db.relationship('Log', backref='user', lazy=True)
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    user_name = db.Column(db.String(50))
    user_role = db.Column(db.String(50))
    user_photo = db.Column(db.String(50))

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log_user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    date_time = db.Column(db.String(50))
