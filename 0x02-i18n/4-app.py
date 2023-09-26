#!/usr/bin/env python3
"""This module contains a basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
from pytz import timezone


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Creates a configuration for the app"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Gets the best language for user"""
    if 'locale' in request.args:
        lang = request.args.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """This is the index route"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
