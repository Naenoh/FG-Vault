from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_caching import Cache
from werkzeug.contrib.fixers import ProxyFix
import os

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
# Loads the default/production configuration
app.config.from_pyfile('default_config.py')

# Loads specific dev config, if it exists
app.config.from_pyfile('dev_config.py', True)

db = SQLAlchemy(app)
CORS(app)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

from app import models

