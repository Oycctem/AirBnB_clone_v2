#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def imanumber2(n):
    """ Returns if an int is odd or even """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
