from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
import os

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
if os.environ.get('ENV','') == 'production':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(os.environ['POSTGRES_DB_USER'],
                                                                                 os.environ['POSTGRES_DB_PWD'],
                                                                                 os.environ['POSTGRES_DB_HOST'],
                                                                                 os.environ['POSTGRES_DB_PORT'],
                                                                                 os.environ['POSTGRES_DB_NAME'])
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fgctechuser:fgctechpass10@127.0.0.2:5431/fgctech'  # TODO hide this
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

from app import models

