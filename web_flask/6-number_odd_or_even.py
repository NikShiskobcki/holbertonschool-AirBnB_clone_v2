#!/usr/bin/python3
"""task 1"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """say hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display c"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display python"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    """display template"""
    return render_template("5-number.html", var=n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """display odd or even"""
    if (n % 2) == 0:
        var = "even"
    else:
        var = "odd"
    return render_template("6-number_odd_or_even.html",
                           n=n, var=var)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
