#!/usr/bin/python3
"""
This module defines a Flask web application
with various routes for different purposes.
"""

from flask import Flask, render_template

app = Flask(__name__)
"""
This instance of the Flask class initializes the Flask web application.
"""


@app.route('/', strict_slashes=False)
def hello():
    """
    Displays 'Hello HBNB!' when navigating to the root URL.

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when navigating to the '/hbnb' URL.

    Returns:
        str: The string 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Displays 'C ' followed by the provided text.
    Spaces replace underscores in the text.

    Args:
        text (str): The text to be displayed.

    Returns:
        str: The concatenated string of 'C ' and the modified text.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Displays 'Python ' followed by the provided text.
    Spaces replace underscores in the text.

    Args:
        text (str): The text to be displayed.

    Returns:
        str: The concatenated string of 'Python ' and the modified text.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays 'n is a number' only if n is an integer.

    Args:
        n (int): The number to be displayed.

    Returns:
        str: The formatted string indicating
        whether the input is a number or not.
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with the content "Number: n" only if n is an integer.

    Args:
        n (int): The number to be displayed in the HTML page.

    Returns:
        str: The HTML page with the content "Number: n".
    """
    return render_template('number_template.html', number=n)


if __name__ == '__main__':
    """
    Starts the Flask web application on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)
