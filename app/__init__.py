from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from flask.ext.principal import (Principal, Permission, identity_loaded, RoleNeed, UserNeed)

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.setup_app(app)
principals = Principal(app)

admin_permission = Permission(RoleNeed('admin'))

from app.users.models import Users


@login_manager.user_loader
def load_user(userid):
    return Users.by_id(userid)


@app.errorhandler(404)
def non_fount(error):
    return render_template('404.html'), 404


@app.route('/', methods=['GET', ])
def handle_splash():
    return render_template('index.html')

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'id'):
        identity.providers.add(UserNeed(current_user.id))

    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.name))
