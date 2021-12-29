from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from flask_login import UserMixin


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author')


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    

    def verify_password(self, password):
        return check_password_hash(password)


    def __repr__(self):
        return '<User %r>' % self.name


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))


@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))