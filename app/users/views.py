import random

from sqlalchemy.exc import IntegrityError
from passlib.hash import pbkdf2_sha256

from flask import (Blueprint, request, render_template, flash, g, session,
    redirect, url_for, json, jsonify, current_app)
from flask.ext.login import (login_user, logout_user, current_user)
from flask.ext.principal import Identity, AnonymousIdentity, identity_changed

from app import db
from app.users.models import Users, Roles

mod = Blueprint('users', __name__, url_prefix='/users')


@mod.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = Users.by_id(session['user_id'])


@mod.route('/login', methods=['GET', 'POST', ])
def login():
    if request.method == 'GET':
        return render_template('users/nonsms_login.html')
    elif request.method == 'POST':
        if request.form.get('username', '').find('@') > 0:
            user = Users.by_email(request.form.get('username', ''))
        else:
            user = Users.by_username(request.form.get('username', ''))
        if user:
            if pbkdf2_sha256.verify(request.form.get('password', ''), user.password):
                session['user_id'] = user.id
                session['phone'] = user.phone
                login_user(user)
                identity_changed.send(current_app._get_current_object(),
                    identity=Identity(user.id))

                return redirect(url_for('STUFF'))
        else:
            return redirect(url_for('handle_splash'))


@mod.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('users/register.html')
    elif request.method == 'POST':
        name = request.form.get('name', '')
        username = request.form.get('username', '')
        email = request.form.get('email', '')
        password = pbkdf2_sha256.encrypt(request.form.get('password', ''), rounds=8000, salt_size=10)
        user = Users(name=name, username=username, email=email, password=password)
        #  TODO: Make more flexible based on the UI for this view
        if request.form.get('role', '') == "2":
            role = Roles.by_id(2)
            user.roles.append(role)
        db.session.add(user)
        db.session.commit()
        if not current_user.is_anonymous():
            return redirect(url_for('STUFF'))
        else:
            return redirect(url_for('handle_splash'))
