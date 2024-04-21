#!/usr/bin/python3
"""
This module defines a Flask web application with several routes, each demonstrating
simple text responses with dynamic route parameters and default values.
- /: Displays 'Hello HBNB!'
- /hbnb: Displays 'HBNB'
- /c/<text>: Displays 'C <text>', underscores in text are replaced by spaces
- /python/(<text>): Displays 'Python <text>', with 'is cool' as the default text, underscores are replaced by spaces
"""
from flask import Flask

app = Flask(__name__)
"""
This instance of the Flask class initializes the web application.
Handles routing and responses, managing web requests according to the defined routes.
"""


@app.route('/', strict_slashes=False)
def hello():
    """ Displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Displays 'C ' followed by the text, spaces replace underscores """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Displays 'Python ' followed by the text, spaces replace underscores """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
