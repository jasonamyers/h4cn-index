import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['', ])
SECRET_KEY = 'ksvnnaJcUH2D'
SQLALCHEMY_DATABASE_URI = 'psycopg2+postgres://u2m0jgp68pevsd:p390mu1qaogbrb6hhmnil46sukd@ec2-23-21-193-88.compute-1.amazonaws.com:5432/d3ibj7prohvebf'
SQLALCHEMY_POOL_RECYCLE = 30

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'oGEDRWGGtRI7'
