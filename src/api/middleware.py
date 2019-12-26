import os
from functools import wraps
from flask import g
from redis import Redis


def init_redis(f):
    @wraps(f)
    def initiate(*args, **kwargs):
        if 'redis' not in g:
            g.redis = Redis(host=os.environ.get('REDIS_HOST', 'localhost'), port=6379, db=0)
        return f(*args, **kwargs)
    return initiate
