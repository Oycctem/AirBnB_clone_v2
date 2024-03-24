#!/usr/bin/python3
""" Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """ Returns 'is a number' if n is an int """
    return '{:d} is a number'.format(n)


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
