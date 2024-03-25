#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/number_template/<int:n>', strict_slashes=False)
def imanumber(n):
    """ Returns HTML page only if n is an int """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
