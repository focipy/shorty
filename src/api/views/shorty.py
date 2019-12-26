"""
Shorty API module.
"""
import random
import string

from flask import jsonify, request, g, redirect, render_template
from flask.views import MethodView
from marshmallow import ValidationError
from redis import Redis

from api import init_redis
from api.schemas import ShortyPostSchema

URL_LENGTH = 5


class Shorty(MethodView):

    def get(self):
        return render_template('index.html')

    @init_redis
    def post(self):
        data = request.json
        try:
            data = ShortyPostSchema().load(data)
        except ValidationError as e:
            return jsonify(e.messages)

        if custom_link := data.get('custom'):
            if stored_url := g.redis.get(custom_link):
                if data['url'] != stored_url.decode():
                    return jsonify({'error': 'The custom link is already taken.'})
            g.redis.set(custom_link, data['url'])
            return jsonify({'link': request.base_url + custom_link})

        if existing_uid := g.redis.get(data['url']):
            return jsonify({'link': request.base_url + existing_uid.decode()})

        # ToDo: Using random is not efficient to get a short URL. Requires an algorithm.
        random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=URL_LENGTH))
        is_taken = g.redis.get(random_key)
        while is_taken is not None:
            random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=URL_LENGTH))
            is_taken = g.redis.get(random_key)

        # ToDo: Currently setting two keys to redis. Can probably find a way to use a single hashmap key.
        g.redis.set(random_key, data['url'])
        g.redis.set(data['url'], random_key)

        return jsonify({'link': request.base_url + random_key})


class ShortyURL(MethodView):
    @init_redis
    def get(self, req_uid):
        if link := g.redis.get(req_uid):
            return redirect(link.decode(), code=302)
        return jsonify({'error': 'No url /%s exists.' % req_uid})
