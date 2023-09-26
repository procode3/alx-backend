#!/usr/bin/env python3
"""This module contains a basic flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Creates a configuration for the app"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """Gets the best language for user"""
    settings = g.get('user_locale')
    query = request.args.get('locale')
    header = request.accept_languages.best_match(app.config['LANGUAGES'])
    if 'locale' in request.args and query in app.config['LANGUAGES']:
        return query
    elif settings and settings in app.config['LANGUAGES']:
        return settings
    elif header:
        return header
    else:
        return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """This is the index route"""
    user = g.user
    return render_template('5-index.html', user=user)


def get_user():
    """Gets a user or returns None if no user"""
    if 'login_as' not in request.args:
        return None
    return users.get(int(request.args['login_as']))


@app.before_request
def before_request():
    """sets a user as global context"""
    user = get_user()
    g.user = user


if __name__ == '__main__':
    app.run()
