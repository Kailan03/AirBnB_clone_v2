#!/usr/bin/python3
"""
A simple Flask web application
This module starts a Flask web server that listens on 0.0.0.0, port 5000.
It includes a route that displays a greeting message.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    Root endpoint that returns a greeting message.
    Accessible without strict slashes, meaning both / and / (trailing slash) will work.
    Returns:
        A string saying "Hello HBNB!"
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

