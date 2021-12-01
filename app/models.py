from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {},{}>'.format(self.username,self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_use(id):
    return User.query.get(int(id))

class statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headshots = db.Column(db.String(64))
    kills = db.Column(db.String(64))
    bestKD = db.Column(db.String(64))
    bestWL = db.Column(db.String(64))
    bestSR = db.Column(db.String(64))


    def __repr__(self):
        return '<User {}>'.format(self.id)




