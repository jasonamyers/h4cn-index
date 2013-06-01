import datetime
import calendar
from flask.ext.login import UserMixin
from app import db

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))

class Roles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    @classmethod
    def by_id(cls, role_id):
        return db.session.query(Roles).filter(Roles.id == role_id).first()

    @classmethod
    def get_roles(cls):
        return db.session.query(Roles).all()


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(1000))
    email = db.Column(db.String(255), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    active = db.Column(db.Boolean(), default=True)
    timezone = db.Column(db.String(1000), default=None, nullable=True)
    roles = db.relationship('Roles', secondary=roles_users,
        primaryjoin=id == roles_users.c.user_id, backref='users')

    def __init__(self, name=None, email=None, username=None, password=None, active=True, timezone='CST6CDT'):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.active = active
        self.timezone = timezone

    @classmethod
    def by_id(cls, user_id):
        return db.session.query(Users).filter(Users.id == user_id).first()

    @classmethod
    def by_username(cls, username):
        return db.session.query(Users).filter(Users.username == username).first()

    @classmethod
    def by_email(cls, email):
        return db.session.query(Users).filter(Users.email == email).first()
