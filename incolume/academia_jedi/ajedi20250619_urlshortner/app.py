"""Module urlshortner."""

from __future__ import annotations

import os
import random
import string

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from icecream import ic

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    """Create tables."""
    db.create_all()


class Urls(db.Model):
    """Url class."""

    id_ = db.Column('id_', db.Integer, primary_key=True)
    long = db.Column('long', db.String())
    short = db.Column('short', db.String(10))

    def __init__(self, long, short):
        """Init class."""
        self.long = long
        self.short = short


def shorten_url():
    """Shorten url."""
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = ''.join(rand_letters)
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters


@app.route('/', methods=['POST', 'GET'])
def home():
    """Route home."""
    if request.method == 'POST':
        url_received = request.form['nm']
        found_url = Urls.query.filter_by(long=url_received).first()

        if found_url:
            return redirect(url_for('display_short_url', url=found_url.short))
        short_url = shorten_url()
        ic(short_url)
        new_url = Urls(url_received, short_url)
        db.session.add(new_url)
        db.session.commit()
        return redirect(url_for('display_short_url', url=short_url))
    return render_template('url_page.html')


@app.route('/<short_url>')
def redirection(short_url):
    """Route redirect."""
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    return '<h1>Url doesnt exist</h1>'


@app.route('/display/<url>')
def display_short_url(url):
    """Route display short."""
    return render_template('shorturl.html', short_url_display=url)


@app.route('/all_urls')
def display_all():
    """Route display all."""
    return render_template('all_urls.html', vals=Urls.query.all())


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # noqa: S201
