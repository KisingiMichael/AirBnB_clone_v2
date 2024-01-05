#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Display C followed by the value of <tet>"""
    """Replace underscores with spaces in the text"""
    formatted_text = text.replace('_', ' ')
    return "C {}". format(formatted_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """Display "Python is cool" """
    formatted_python_text = text.replace('_', ' ')
    return "Python {}".format(formatted_python_text)


@app.route('/number/<int:n>', strict_slashes=False)
def numbers(n):
    """Display if n is number """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display HTML if n is a number"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display odd or even number in HTML"""
    """check if provided number is integer"""
    if isinstance(n, int):
        even_or_odd = "even" if n % 2 == 0 else "odd"
        return render_template('6-number_odd_or_even.html',
                               n=n, even_or_odd=even_or_odd)
    else:
        """Return error if not number supplied"""
        return "Invalid input. Please provide an integer"


if __name__ == "__main__":
    """Start the Flask developement server"""
    app.run(host='0.0.0.0', port=5000)
