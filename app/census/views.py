from flask import (Blueprint, request, render_template, flash, g, session,
    redirect, url_for, json, jsonify, current_app)
from flask.ext.login import (login_user, logout_user, current_user)
from flask.ext.principal import Identity, AnonymousIdentity, identity_changed

from sqlalchemy import create_engine
from sqlalchemy.sql import select, func

from app import db
from config import SQLALCHEMY_DATABASE_URI
from app.users.models import Users, Roles
from app.census.datahelpers import build_table

mod = Blueprint('census', __name__, url_prefix='/census')


@mod.before_request
def before_request():
    g.conn = create_engine(SQLALCHEMY_DATABASE_URI)
    g.t = None
    g.t = build_table('census')


@mod.route('', methods=['GET', ])
def census():
    return render_template('census/index.html')


@mod.route('/test', methods=['GET', ])
def census_test():
    values = {}
    s = select(
        [
            g.t.c.type,
            g.t.c.district,
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], g.t.c.race != 'ALL').group_by(
            g.t.c.type,
            g.t.c.district,
            g.t.c.race,
            g.t.c.factor).order_by(
                g.t.c.type,
                g.t.c.district,
                g.t.c.race,
                g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    for result in results:
        type = getattr(result, 'type')
        if not values.get(type):
            print "resetting type"
            values[type] = {}
        district = getattr(result, 'district')
        if not values[type].get(district):
            print "district reset"
            values[type][district] = {}
        race = getattr(result, 'race')
        if not values[type][district].get(race):
            print "race reset"
            if getattr(result, 'summed'):
                values[type][district][race] = {}
        if getattr(result, 'summed'):
            values[type][district][race] = getattr(result, 'summed')

    return render_template('census/test.html', values=values)


@mod.route('/poverty_by_district/<district_name>', methods=['GET', ])
def census_proverty_by_district(district_name):
    values = {}
    s = select(
        [
            g.t.c.race,
            g.t.c.factor,
            func.sum(g.t.c.value).label('summed')
        ], g.t.c.race != 'ALL').where(
            g.t.c.factor in ['ALL', 'POVERTY'] and
            g.t.c.district == district_name and
            g.t.c.summed != 0).group_by(
                g.t.c.race,
                g.t.c.factor).order_by(
                    g.t.c.race,
                    g.t.c.factor)
    results = g.conn.execute(s).fetchall()
    print results
    for value in results:
        race = getattr(value, 'race')
        if not values.get(race):
            values[race] = {}
        factor = getattr(value, 'factor')
        values[race][factor] = value.summed

    return render_template('census/test.html', values=values, district=district_name)
