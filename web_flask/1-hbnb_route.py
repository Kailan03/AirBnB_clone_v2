#!/usr/bin/python3
"""
This module starts a Flask web application with specific routing rules.

Routes:
- /: Displays 'Hello HBNB!'
- /hbnb: Displays 'HBNB'
"""

from flask import Flask

app = Flask(__name__)
"""
This instance of the Flask class initializes your application.
It acts as the central object that all configurations,
routes, and more will be registered with.
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
