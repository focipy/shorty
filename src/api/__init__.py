"""
API module

Creates the Flask App, CORS for
options and registers the blueprints.
"""

import os

from flask import Flask
from flask_cors import CORS

from .middleware import init_redis
from .views.shorty import Shorty, ShortyURL


URL_PREFIX = os.environ.get('URL_PREFIX', '/shorty')

app = Flask(__name__)
CORS(app)

app.add_url_rule(URL_PREFIX + '/', view_func=Shorty.as_view('shorty'))

app.add_url_rule(URL_PREFIX + '/<req_uid>', view_func=ShortyURL.as_view('shorty_url'))
