#!/usr/bin/python3
"""
This module defines a Flask web application with three routes:
- /: Displays 'Hello HBNB!'
- /hbnb: Displays 'HBNB'
- /c/<text>: Displays 'C ' followed by the text parameter,
with underscores replaced by spaces.
"""
from flask import Flask

app = Flask(__name__)
"""
This instance of the Flask class initializes the web application.
Flask applications handle routing and responses,
managing requests according to the defined paths.
"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" when navigating to the root URL.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" when navigating to '/hbnb' URL.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Display "C " followed by the text.
    Underscores in 'text' are replaced with spaces.
    """
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
