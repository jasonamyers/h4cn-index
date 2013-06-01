import random

from sqlalchemy.exc import IntegrityError
from passlib.hash import pdkdf2_sha256

from flask import (Blueprint, request, render_template, flash, g, session,
    redirect, url_for, json, jsonify, current_app)
from flask.ext.login import (login_user, logout_user, current_user)
from flask.ext.pricipal import Identity, AnonymousIdentity, indentity_changed

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

                return "Stuff"
