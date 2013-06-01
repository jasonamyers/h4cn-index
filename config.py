import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['', ])
SECRET_KEY = 'ksvnnaJcUH2D'
SQLALCHEMY_POOL_RECYCLE = 30

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'oGEDRWGGtRI7'
